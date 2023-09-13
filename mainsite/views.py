#from django.shortcuts import render (原始檔)

# Create your views here.
# 以下為更新內容

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from datetime import datetime

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


def index(request):     #建完index.html後手動新增
    posts = Post.objects.all()
    now = datetime.now()
    number = 1
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