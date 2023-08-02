#from django.shortcuts import render (原始檔)

# Create your views here.
# 以下為更新內容

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from datetime import datetime

# Create your views here.
def homepage(request):
    posts = Post.objects.all() # 繼承了.models 查詢(撈)資料庫全資料 , posts=[Instance(1), Instance(2)...]
    post_lists = list() #建立list 資料結構

    #把查詢到的資料從頭到尾看一次, 並儲存成list 結構
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>") # str(post) 相當於 str(post.title)
                                                                        # 因為在 models.py 有定義 self=self.title
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")  #p.26的更動, 顯示資料body

        #轉換成html
    return HttpResponse(post_lists) #把回傳的list變成加入 html代碼以網頁結構文法的一部份


def index(request):     #建完index.html後手動新增
    posts = Post.objects.all()
    now = datetime.now()
    number = 1
    return render(request, 'index.html', locals()) #django的函數, index.html為templates的檔名, 將所有變數打包成字點檔