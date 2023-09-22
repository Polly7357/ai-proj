#from django.shortcuts import render (原始檔)

# Create your views here.
# 以下為更新內容

from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from datetime import datetime
from django.db import connection
from django.db.utils import OperationalError
from django.http import JsonResponse


# Create your views here.
def homepage(request):
    posts = Post.objects.all() # 繼承了.models 查詢(撈)資料庫全資料 , posts=[Instance(1), Instance(2)...]
    post_lists = list() #建立list 資料結構

    #把查詢到的資料從頭到尾看一次, 並儲存成list 結構
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>") # str(post) 相當於 str(post.title)
                                                                        # 因為在 models.py 有定義 self=self.title
        #post_lists.append("<small>"+str(post.body)+"</small><br><br>")  #p.26的更動, 顯示資料body

        #轉換成html
    return HttpResponse(post_lists) #把回傳的list變成加入 html代碼以網頁結構文法的一部份


def index(request):
    posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index.html', locals()) #django的函數, index.html為templates的檔名, 將所有變數打包成字點檔

from django.shortcuts import redirect   #0807新增

def showpost(request, slug):        #0807新增, slug來自於urls.py slug冒號後的參數
    try:                            #會先試著執行, 有例外再跳到except
        post = Post.objects.get(slug = slug)    #get(查詢的條件) (查詢的欄位=查詢的值)
       
        if post != None :           #若查詢回傳的不是空物件 None表示找不到
            return render(request, 'pages/post.html', locals())
    except:
        return redirect('/')        #回到127.0.0.1:8000

    return True

def apiTestView(request):
    return render(request, 'pages/apiTest.html', locals())


def customSqlQueryView(request):
    try:
        sql_query = "SELECT timestmp, response FROM plug_info order by timestmp;"

        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()
        
        if not result:
            return JsonResponse({"error": "Table is empty."})

        # Process the result as needed and return a JSON response
        data = [{'timestamp': row[0], 'info': row[1]} for row in result]
        return JsonResponse({'data': data})
    except OperationalError as e:
        return JsonResponse({"error":f"DB error:{e}"})
    except Exception as e:
        return JsonResponse({"error":f"error occurred:{e}"})
    
def index2_post(request):
    #posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index2.html', locals())

def index3_post(request):
    #posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index3.html', locals())

def index4_post(request):
    #posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index4.html', locals())

def index5_post(request):
    #posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index5.html', locals())

def index6_post(request):
    #posts = Post.objects.all()
    #now = datetime.now()
    return render(request, 'pages/index6.html', locals())