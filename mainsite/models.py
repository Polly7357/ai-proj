from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200)
    body = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:  #以最新日期排序-負向排序
        ordering = ('-pub_date',)

    def __str__(self):  #查詢回應一條詢息
        return self.title
