from django.shortcuts import render

# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from bolgtext1.models import BolgPost
from bolgtext1.models import Richang
def index(request):
    #return HttpResponse('hello django')
    return HttpResponse(render(request,'index.html'))

def mybolg(request):
    posts = BolgPost.objects.all()
    t = loader.get_template('mybolg.html')
    c= Context({'posts':posts})
    return HttpResponse(t.render(c ))

def richang(request):
    posts = Richang.objects.all()#貌似数据库名必须大写
    t = loader.get_template('richang.html')
    c = Context({'posts': posts})
    return HttpResponse(t.render(c))
def tubiao(request):
    return HttpResponse('/static/favicon.ico')

