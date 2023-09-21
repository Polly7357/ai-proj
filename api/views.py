from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse, HttpResponseServerError, HttpResponseNotFound
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from json.decoder import JSONDecodeError  # Import JSONDecodeError for handling JSON parsing errors
from datetime import datetime
from mainsite.models import *
import json, os
import sqlite3

#create view here

def test(request):
    #呈現的 Json資料
    data = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    response = JsonResponse(data, status=200) # 代號200表成功
    return response

# electricity_calculator/views.py
@csrf_exempt
def calculate_electricity_cost_view(request):

    cases = ['Reality','Smartly']
    case_usage={}

    # Check if the request contains JSON data
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)
        except json.JSONDecodeError as e:
            return JsonResponse({"error": "Invalid JSON data in the request"}, status=400)
    else:
        # 假如前端沒送正確Json就使用file
        json_file_path = "user_data_house_perday.json"
        if not os.path.exists(json_file_path):
            return JsonResponse({"error": "File does not exist"}, status=400)
        elif os.path.getsize(json_file_path) == 0:
            return JsonResponse({"error": "File is empty"}, status=400)
        else:
            with open(json_file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)


    for case in cases:
        if case == 'Reality':
            json_file_path = "user_data_house_perday.json"

        elif case == 'Smartly':
            json_file_path = "suggest_user_data.json"


        try:
            # Check if "user_data.json" file exists      
            if not os.path.exists(json_file_path):
                return JsonResponse({"error": "File does not exist"}, status=400)
            else:
                print(json_file_path,'file exist.')

            # Check if "user_data.json" file is empty
            if os.path.getsize(json_file_path) == 0:
                return JsonResponse({"error": "File is empty"}, status=400)
            else:
                print(json_file_path,'file is not empty.')

            # Read JSON data from the "user_data.json" file
            with open(json_file_path, "r", encoding="utf-8") as json_file:
                json_data = json.load(json_file)
            #    print(json_data)


            tables = ["c2_rates", "c3_rates", "summer_c2_rates", "summer_c3_rates"]
            usage_data={}
            usage_list={}
            user_id = json_data['id']
            cal_time = round(datetime.now().timestamp())

            for table in tables:
                electricity, electricity_cost, wend_cost = calculate_electricity_cost(json_data, 'db.sqlite3', table)
                monthly_consumption, monthly_costs = monthly_usage(electricity, electricity_cost, wend_cost)
                
                match table:
                    case 'c2_rates':
                        pricing = 'TwoTier'
                    case 'c3_rates':
                        pricing = 'ThreeTier'
                    case 'summer_c2_rates':
                        pricing = 'TwoTierSummer'                    
                    case 'summer_c3_rates':
                        pricing = 'ThreeTierSummer'                    
                    
                if electricity_cost is not None:
                    #print(f"\nTable: {table}")
                    #print(f"單日用電約: {electricity:.2f} kWh; 單日電費約 {electricity_cost:.2f} 元; 週末電費約 {wend_cost:.2f} 元")
                    #print(f'月估用電約: {monthly_consumption:.2f} 度; 月電費約 {monthly_costs:.2f} 元')
                    #print(f'使用表燈累進式費率, 月電費約 2469 元')
                                # Prepare the response data
                    electricity = round(electricity,2)
                    electricity_cost = round(electricity_cost,2)
                    wend_cost = round(wend_cost,2)
                    monthly_consumption = round(monthly_consumption,2)
                    monthly_costs =round(monthly_costs,2)

                    usage_data[pricing] = {
                        "DailyCost": electricity_cost,
                        "WeekendCost": wend_cost,
                        "MonthlyCost": monthly_costs,
                    }
                    #usage_list.append(usage_data)

                else:
                    #print(f"Unable to calculate electricity cost for {table}.")
                    return JsonResponse({"error": str(e)}, status=400)
                
            #calculte cdf of monthly elec consumption    
            elec_cdf = elec2cdf (monthly_consumption)    
            case_usage[case]={
                "MonthlyElectricity":monthly_consumption,
                "MonthlyCarbonEmission": elec_cdf,
                "Priciing":usage_data}
                


        except Exception as e:
            print("An error occurred:", str(e))
            return JsonResponse({"error orrurs": str(e)}, status=400)
        
    response_data ={
    "Source": user_id,
    "EntryTime": cal_time,
    "DailyElectricity": electricity,
    # "Monthly-Electricity": monthly_consumption,
    # "Monthly-Carbon-Emission": elec_cdf,
    "case": case_usage,
    }

    return JsonResponse(response_data, status=200)




def calculate_electricity_cost(json_data, database_path, table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Initialize total cost
        total_cost = 0.0
        total_power = 0

        # Iterate through the JSON data
        for device_usage in json_data['usage']:
            device_name = device_usage["device_name"]
            start_hour = int(device_usage["start_hour"])
            end_hour = int(device_usage["end_hour"])

            # check_point
            #print(device_usage["device_name"], end=' : ')

            # Query the elec_device_consumption table to get the power consumption for the device
            cursor.execute("SELECT watt FROM elec_device_consumption WHERE name = ?", (device_name,))
            row = cursor.fetchone()
            if row is not None:
                power_consumption = row[0]  # Get the power consumption in watts

                # check_point
                #print(power_consumption, end=' ==> ')                

                # 自不同費率表讀取時段與費率
                cursor.execute(f"SELECT wday_rate, wend_rate FROM {table_name} WHERE h_id BETWEEN ? AND ?",
                            (start_hour, end_hour))
                results = cursor.fetchall()

                # 功率轉換成度
                unit_power = power_consumption / 1000  # Convert watts to kilowatts
                total_hours = end_hour - start_hour + 1

                # check_point
                #print(f'{unit_power} (kwh) *',end=' ')
                #print(total_hours,'hours') 

                for row in results:
                    wday_rate = row[0]  # Extract wday_rate
                    wend_rate = row[1]
                    if wday_rate is not None:
                        # 將取得的費率mapping到電價
                        cursor.execute("SELECT rates FROM time_elec_rates WHERE desc = ?", (wday_rate,))
                        rate = cursor.fetchone()

                        cursor.execute("SELECT rates FROM time_elec_rates WHERE desc = ?", (wend_rate,))
                        end_rate = cursor.fetchone()

                        
                        if rate is not None:
                            rate = rate[0]
                            total_cost += unit_power * rate
                total_power += unit_power * total_hours
                
                # 計算週末電費
                wend_cost = total_power * end_rate[0]

        # Close the database connection
        conn.close()

        return total_power, total_cost, wend_cost

    except sqlite3.Error as e:
        print("SQLite error:", e)                                                                   
        return None
        
def monthly_usage(electricity, electricity_cost, wend_cost):
    monthly_elec = electricity * 30
    monthly_cost = (electricity_cost * 26) + (wend_cost * 4) + 75
    return monthly_elec, monthly_cost

def elec2cdf(electricity):
    try:
    # Connect to the SQLite database
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        cursor.execute("SELECT cde FROM energy WHERE id = 'c1s01i137'")
        row = cursor.fetchone()
        if row is not None:
            Cde = row[0]
            elec2cdf = electricity * Cde
            return elec2cdf
        
    except sqlite3.Error as e:
        print("SQLite error:", e)                                                                   
        return None

# Read JSON data from file "user_data.json"
# with open("user_data.json", "r", encoding="utf-8") as json_file:
#     json_data = json.load(json_file)

#database_path = ''  # Database file path


# /api/devices/
def showdevice(request):        
    try:                            #會先試著執行, 有例外再跳到except
        devices = ElecDeviceConsumption.objects.all()    #get(查詢的條件) (查詢的欄位=查詢的值)
       
        if devices != None :           #若查詢回傳的不是空物件 None表示找不到
            return render(request, 'pages/elec_device.html', locals())
    except:
        return redirect('/')        #回到127.0.0.1:8000

    return True


# api/power/accu_usage/

def calculate_accumulative_usage(total_expense):
    # 定義非夏季、夏季費率表
    rate_table_non_summer = [
        (120, 1.63),   
        (210, 2.10), 
        (220, 2.89), 
        (150, 3.94), 
        (300, 4.74),     # Usage from 701 to 1000 degrees, price 4.80元 per degree (1000-701)
        (3000, 6.03)     # Usage from 501 to 700 degrees, price 4.80元 per degree (?-1001)
    ]

    rate_table_summer = [
        (120, 1.63),    # Usage up to 120 degrees, price 1.63元 per degree
        (210, 2.38),    # Usage from 121 to 330 degrees, price 2.38元 per degree (331-120)
        (220, 3.52),    # Usage from 331 to 500 degrees, price 3.52元 per degree (551-330)
        (150, 4.80),     # Usage from 501 to 700 degrees, price 4.80元 per degree (701-550)
        (300, 5.83),     # Usage from 701 to 1000 degrees, price 4.80元 per degree (1000-701)
        (3000, 7.69)     # Usage from 501 to 700 degrees, price 4.80元 per degree (?-1001)
    ]


    # 依電費回推用電量
    def calculate_degrees(expense, rate_table):
        degrees_used = 0
        remaining_expense = expense/2   #帳單電費為2個月總計

        for limit, rate in rate_table:
            if remaining_expense <= 0:
                break

            if remaining_expense >= limit * rate:
                degrees_used += limit
                remaining_expense -= limit * rate
            else:
                degrees_used += remaining_expense / rate
                remaining_expense = 0

        return degrees_used

    # Calculate degrees for non-summer season
    degrees_non_summer = calculate_degrees(total_expense, rate_table_non_summer)

    # Calculate degrees for summer season
    degrees_summer = calculate_degrees(total_expense, rate_table_summer)

    # Prepare the context to pass to the template
    return {
        'degrees_non_summer': round(degrees_non_summer,2),
        'degrees_summer': round(degrees_summer,2),
    }


# api/power/accu_usage/
def calculate_accumulative_usage_view(request):
    if 'total_expense' in request.GET:
        total_expense = float(request.GET['total_expense'])
        result = calculate_accumulative_usage(total_expense)
        return JsonResponse(result)
    else:
        return JsonResponse({'error': 'total_expense parameter is missing in the request.'}, status=400)




# 從使用度數推算累進費率
def calculate_accumulative_cost(usage):

    # 定義累進式非夏季、夏季費率表
    rate_table_non_summer = [
        (120, 1.63),
        (210, 2.10),
        (220, 2.89),
        (150, 3.94),
        (300, 4.74),
        (3000, 6.03)
    ]

    rate_table_summer = [
        (120, 1.63),
        (210, 2.38),
        (220, 3.52),
        (150, 4.80),
        (300, 5.83),
        (3000, 7.69)
    ]


    def calculate_cost(usage, rate_table):
        electricity_price = 0

        for limit, price_per_degree in rate_table:
            if usage <= limit:
                electricity_price += usage * price_per_degree
                break
            else:
                electricity_price += limit * price_per_degree
                usage -= limit

        return electricity_price
    
    electricity_cost_non_summer = calculate_cost(usage, rate_table_non_summer)
    electricity_cost_summer = calculate_cost(usage, rate_table_summer)
    
    return {
        'monthly_elec_cost_non_summer': electricity_cost_non_summer,
        'monthly_elec_cost_summer': electricity_cost_summer
    }

# api/power/accu_cost
# 從使用度數推算累進費率 Http request view
def calculate_accumulative_cost_view(request):
    if 'usage' in request.GET:
        usage = int(request.GET['usage'])
        electricity_cost = calculate_accumulative_cost(usage)
        return JsonResponse(electricity_cost)
    else:
        return JsonResponse({'error': 'usage parameter is missing in the request.'}, status=400)

import json
from mainsite.models import Beverage, CdeTransport, LactoseProds, Energy


# 計算消費品碳當量
# api/cde/
def calculate_cde_View(request):

    # Provided JSON data
    data = '''
    {
        "beverage": {
            "瓶裝水(600ml，PET包裝)": 2,
            "可樂(寶特瓶裝，600ml)": 2,
            "奶茶（300ml，鋁箔包裝）": 2,
            "經典台灣啤酒，330 ml (6罐裝，收縮膜)": 1
        },
        "cde_transport": {
            "機器腳踏車": 10
        },
        "lactose_prods": {
            "焦糖烤布丁": 2
        },
        "energy": {
            "電(2022）": 800,
            "臺灣自來水(2017)": 300
        }
    }
    '''


    parsed_data = json.loads(data)

    total_cde_beverage = 0
    total_cde_cde_transport = 0
    total_cde_lactose_prods = 0
    total_cde_energy = 0

    # Calculate total cde for 'beverage' class
    for item_name, quantity in parsed_data.get("beverage", {}).items():
        beverage_obj = Beverage.objects.filter(name=item_name).first()
        if beverage_obj:
            print(f"Found matching item in 'cde_transport': {item_name}")
            total_cde_beverage += beverage_obj.cde * quantity
        else:
            print(f"Item not found in 'beverage': {item_name}")

    # Calculate total cde for 'cde_transport' class
    for item_name, quantity in parsed_data.get("cde_transport", {}).items():
        #移除隱形資料可能的空白
        item_name = item_name.strip()

        #移除db data可能的空白
        #cde_transport_obj = CdeTransport.objects.filter(name=item_name).first()
        cde_transport_obj = CdeTransport.objects.filter(name__iexact=item_name.replace(" ", "")).first()
        if cde_transport_obj:
            print(f"Found matching item in 'cde_transport': {item_name}")
            total_cde_cde_transport += cde_transport_obj.cde * quantity
        else:
            print(f"Item not found in 'cde_transport': {item_name}")
            all_cde_transport_names = CdeTransport.objects.values_list('name', flat=True)
            print(f"All names in CdeTransport objects: {', '.join(all_cde_transport_names)}")

    # Calculate total cde for 'lactose_prods' class
    for item_name, quantity in parsed_data.get("lactose_prods", {}).items():
        lactose_prods_obj = LactoseProds.objects.filter(name=item_name).first()
        if lactose_prods_obj:
            print(f"Found matching item in 'beverage': {item_name}")
            total_cde_lactose_prods += lactose_prods_obj.cde * quantity
        else:
             print(f"Item not found in 'lactose_prods': {item_name}")

    # Calculate total cde for 'energy' class
    for item_name, quantity in parsed_data.get("energy", {}).items():
        energy_obj = Energy.objects.filter(name=item_name).first()
        if energy_obj:
            print(f"Found matching item in 'beverage': {item_name}")
            total_cde_energy += energy_obj.cde * quantity
        else:
            print(f"Item not found in 'energy': {item_name}")

    # Prepare the response data as a dictionary
    response_data = {
        "total_cde_beverage": total_cde_beverage,
        "total_cde_cde_transport": round(total_cde_cde_transport,3),
        "total_cde_lactose_prods": total_cde_lactose_prods,
        "total_cde_energy": total_cde_energy,
    }

    # Return the response as JSON
    return JsonResponse(response_data)

from api.models import *

def sensor_data(request):
    mac_address = request.GET['m']
    sensor_type = request.GET['t']
    sensor_value = request.GET['v']


    sensor = Sensor( source_mac = mac_address, sensor_type = sensor_type, sensor_value = sensor_value)
    sensor.save();


    data = { 'msg' : 'OK', 'id': sensor.id}
    response = JsonResponse(data, status=200)
    return response



# api/smart_plug/ 
# import sqlite3
@csrf_exempt
def showPlugInfoView(request):
    database_path = 'db.sqlite3'
    current_time = datetime.now()

    custom_sql_query = """
    SELECT timestmp, response
    FROM plug_info
    ORDER BY timestmp DESC
    """

    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()

        # Execute the custom SQL query
        cursor.execute(custom_sql_query)

        # Fetch the data from the cursor
        data = cursor.fetchall()

        if not data:
            # Handle the case where there is no data
            return HttpResponseNotFound("No data found in the database")        

        processed_data = []  # To store processed data

        print('筆數:',len(data))
        for row in data:
            timestamp = row[0]
            response = row[1]

            try:
                response_data = json.loads(response)

                # Process the data as needed
                # processed_data.append({
                #     'timestamp': timestamp,
                #     'items': response  # Include the response data as it is
                # })

                # Process the additional item_data here
                for item_data in response_data:
                    name = item_data['itemData']['name']
                    mac = item_data['itemData']['extra']['mac']
                    online = item_data['itemData']['online']
                    current = item_data['itemData']['params']['current']
                    voltage = item_data['itemData']['params']['voltage']
                    power = item_data['itemData']['params']['power']
                    monthKwh = item_data['itemData']['params'].get('monthKwh', None)
                    dayKwh = item_data['itemData']['params'].get('dayKwh', None)

                    # Now you can use the time_difference and other data as needed
                    processed_data.append({
                        'timestamp': timestamp,
                        'items': response,  # Include the response data as it is
                        # 'time_difference': time_difference.total_seconds(),  # Time difference in seconds
                        'name': name,
                        'mac': mac,
                        'online': online,
                        'current': current,
                        'voltage': voltage,
                        'power': power,
                        'monthKwh': monthKwh,
                        'dayKwh': dayKwh
                    })
            except JSONDecodeError:
                # Handle JSON parsing errors
                return HttpResponseServerError("Error parsing JSON data")

        # You can choose to return a POST request response or render a template
        if request.method == 'POST':
            # If it's a POST request, return a JSON response
            return JsonResponse(processed_data, safe=False)
        else:
            # If it's not a POST request, render a template
            return render(request, 'pages/pluginfo.html', {'processed_data': processed_data})

    except Exception as e:
        # Handle other exceptions
        return HttpResponseServerError("An error occurred: {}".format(str(e)))

    finally:
        # Close the database connection
        cursor.close()
        conn.close()




