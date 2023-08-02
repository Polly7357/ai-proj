#from django.shortcuts import render (原始檔)

# Create your views here.
# 以下為更新內容

from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.
def homepage(request):
    posts = Post.objects.all() #查詢(撈)資料
    post_lists = list() #建立list 資料結構

    #把查詢到的資料從頭到尾看一次, 並儲存成list 結構
    for count, post in enumerate(posts):
        post_lists.append("No.{}:".format(str(count)) + str(post)+"<br>") 
        post_lists.append("<small>"+str(post.body)+"</small><br><br>")  #p.26的更動, 顯示資料body

        #轉換成html
    return HttpResponse(post_lists) #把回傳的list變成html代碼的一部份