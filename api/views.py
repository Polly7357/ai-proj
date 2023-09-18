from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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
from django.http import JsonResponse


@csrf_exempt
def calculate_electricity_cost_view(request):

    # try:
    #     # Read JSON data from the request (you may need to adjust this based on how you send JSON data to the view)
    #     #json_data = json.loads(request.body)
    cases = ['Reality','Smart']
    case_usage={}

    for case in cases:
        if case == 'Reality':
            json_file_path = "user_data_house_perday.json"

        elif case == 'Smart':
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
                        pricing = '二段式'
                    case 'c3_rates':
                        pricing = '三段式'
                    case 'summer_c2_rates':
                        pricing = '二段式夏季'                    
                    case 'summer_c3_rates':
                        pricing = '三段式夏季'                    
                    
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
                        "單日估算電費(元)": electricity_cost,
                        "週末電費(元)": wend_cost,
                        "整月估計電費(元)": monthly_costs,
                    }
                    #usage_list.append(usage_data)

                else:
                    #print(f"Unable to calculate electricity cost for {table}.")
                    return JsonResponse({"error": str(e)}, status=400)
                
            #calculte cdf of monthly elec consumption    
            elec_cdf = elec2cdf (monthly_consumption)    
            case_usage[case]=usage_data 
                


        except Exception as e:
            print("An error occurred:", str(e))
            return JsonResponse({"error orrurs": str(e)}, status=400)
        
    response_data ={
    "來源": user_id,
    "產生時間": cal_time,
    "單日估算電量(度)": electricity,
    "整月估計電量(度)": monthly_consumption,
    "整月碳排(公斤)": elec_cdf,
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

                # Query the specified rates table to get the rates for the specified hours
                cursor.execute(f"SELECT wday_rate, wend_rate FROM {table_name} WHERE h_id BETWEEN ? AND ?",
                            (start_hour, end_hour))
                results = cursor.fetchall()

                # Calculate total electricity consumption (kWh) for this device
                unit_power = power_consumption / 1000  # Convert watts to kilowatts
                total_hours = end_hour - start_hour + 1

                # check_point
                #print(f'{unit_power} (kwh) *',end=' ')
                #print(total_hours,'hours') 

                for row in results:
                    wday_rate = row[0]  # Extract wday_rate
                    wend_rate = row[1]
                    if wday_rate is not None:
                        # Query the time_elec_rates table to get the rate based on desc
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


def showdevice(request):        #0807新增, slug來自於urls.py slug冒號後的參數
    try:                            #會先試著執行, 有例外再跳到except
        devices = ElecDeviceConsumption.objects.all()    #get(查詢的條件) (查詢的欄位=查詢的值)
       
        if devices != None :           #若查詢回傳的不是空物件 None表示找不到
            return render(request, 'pages/elec_device.html', locals())
    except:
        return redirect('/')        #回到127.0.0.1:8000

    return True

