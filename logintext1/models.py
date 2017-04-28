from django.db import models
from django.contrib import admin

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    email = models.EmailField(max_length=25)
    nicheng = models.CharField(max_length=12)
    def __str__(self):
        username=self.username
        password=self.password
        email=self.email
        nicheng=self.nicheng
        return username,password,email,nicheng
# class User(models.Model):
#     username = models.CharField(max_length=12)
#     password = models.CharField(max_length=12)
#     email = models.EmailField(max_length=25)
#     nicheng = models.CharField(max_length=12)

class Upload(models.Model):
    username = models.CharField(max_length=30)
    headImg = models.FileField(upload_to='./logintext1/static/upload/huanlight/')

    # def __str__(self):
    #     username=self.username
    #     road=self.headImg
    #     return username,road

class UploadAdmin(admin.ModelAdmin):
    list_display = ('username', 'headImg')