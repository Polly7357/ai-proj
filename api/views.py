from django.http import JsonResponse

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