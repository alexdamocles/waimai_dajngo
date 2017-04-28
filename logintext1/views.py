

# Create your views here.
#coding=utf-8
from django.shortcuts import render
from django.template import loader,Context
import pymysql.cursors
from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect,request
from django.template import RequestContext
from django import forms
from logintext1.models  import *
from logintext1 import models
from django.contrib import messages
from django.contrib.messages import add_message
import django.contrib.messages as messages
#表单

#注册表单
class User_regist(forms.Form):
     username = forms.CharField(label='用户名',max_length=12)
     nicheng = forms.CharField(label='昵称',max_length=12)
     password = forms.CharField(label='密码',widget=forms.PasswordInput())
     email = forms.EmailField(label='电子邮箱',max_length=25)

# 登陆表单
class User_login(forms.Form):
     username = forms.CharField(label='用户名',max_length=100)
     password = forms.CharField(label='密码',widget=forms.PasswordInput())

# 上传资料表单
class Upload_zilaio(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    headImg = forms.FileField(label='文件')


#注册
def regist(request):
    if request.method == 'POST':
        uf = User_regist(request.POST)
        if uf.is_valid():
            #获得表单数据

            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            nicheng = uf.cleaned_data['nicheng']
            email = uf.cleaned_data['email']
            #添加到数据库
            User.objects.create(username= username,password=password,)
            #messages.success(request, '注册成功')
            return HttpResponseRedirect('/t/login/')
    else:
        uf = User_regist()

    t = loader.get_template('1_regist.html')
    c = Context({'uf': uf})
    return HttpResponse(t.render(c))

    #return render_to_response('1_regist.html',{'uf':uf}, context_instance=RequestContext(req))

#登陆
def login(request):
    if request.method == 'POST':
        uf = User_login(request.POST)
        if uf.is_valid():
            #获取表单用户密码
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']

            #获取的表单数据与数据库进行比较
            user = User.objects.filter(username__exact = username,password__exact = password)
            print(user)
            if user:
                #比较成功，跳转index
                response = HttpResponseRedirect('/t/user/')
                #将username写入浏览器cookie,失效时间为3600
                response.set_cookie('username',username,3600)
                return response
            else:
                #比较失败，还在login
                return HttpResponseRedirect('/t/login/')
    else:
        uf = User_login()
      # 貌似数据库名必须大写
    t = loader.get_template('1_login.html')
    c = Context({'uf':uf})
    return HttpResponse(t.render(c))
    #return render_to_response('1_login.html',{'uf':uf})

#首页大量模板编辑
def index(request):#需要一个首页滚屏替换
    t1 = loader.get_template('indexwaimai.html')
    c1 = Context({'photo1': 'hahaha'})
    return HttpResponse(t1.render(c1))
    #return HttpResponse(render(request,'indexwaimai.html'))

#登陆成功进入个人中心显示头像和用户名？昵称？
def user(request):
    username = request.COOKIES.get('username','')
    print(username)
    t1 = loader.get_template('user.html')
    c1 = Context({'username': username})
    return HttpResponse(t1.render(c1))
    #return HttpResponse(t.render(username))
    #return render_to_response('1_user.html' ,{'username':username})

#退出注销并清除cookies
def logout(request):
    response = HttpResponse('logout !!')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response

#上传个人资料包括头像
def upload(request):
    if request.method == "POST":
        uf1 = Upload_zilaio(request.POST, request.FILES)
        if uf1.is_valid():
            # 获取表单信息
            username = uf1.cleaned_data['username']
            headImg = uf1.cleaned_data['headImg']

            # 写入数据库
            # 获取表单信息
            username = uf1.cleaned_data['username']
            headImg = uf1.cleaned_data['headImg']
            # 写入数据库
            user = models.Upload(username=username,headImg=headImg)
            # user.username = username
            # user.headImg = headImg
            user.save()
            return HttpResponse('上传成功！')
    else:
        uf1 = Upload()
    return render_to_response('upload.html', {'uf1': uf1})

#当前用户地址列表
def add(request):
    return HttpResponse(render(request,'dizhi_liebiao.html'))

#创建或者修改地址
def create_add(request):
    return HttpResponse(render(request,'dizhi_create.html'))

#个人资料修改
def ziliao(request):
    return HttpResponse(render(request,'dizhi_liebiao.html'))


