#-*- coding:utf-8 -*-
from django.db import models
from django.contrib import admin
# Create your models here.数据库定义表都在这里

class BolgPost(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)


class BolgPostAdmin(admin.ModelAdmin):#更改博客标题(去掉bolgpost)
    list_display = ('title','timestamp')

class Richang(models.Model):#貌似数据库名不许大学
    title = models.CharField(max_length=150)
    body = models.TextField()
    timestamp = models.DateTimeField()
    class Meta:
        ordering = ('-timestamp',)
    class Meta:
        pass
class richnagAdmin(admin.ModelAdmin):
    list_display = ('title', 'timestamp')


class Movie(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    downurl = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        ordering = ('-timestamp',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'body')

# class User(models.Model):
#  username = models.CharField(max_length=50)
#  password = models.CharField(max_length=50)
#  email = models.EmailField()
#orm
# class Text1(models.Model):
#     #id = models.AutoField(primary_key=True)
#     # #可以省略因为不写也可以自动生成#（primary_key=Ture设置为组件)
#     title = models.CharField(max_length=100,null=False)
#     #增加一个字段  名字：title 类型  char 最大长度 100
#     content = models.TextField(null=False)
#     #类型text长度它自己自动
#     link = models.CharField(max_length=100,null=False)
