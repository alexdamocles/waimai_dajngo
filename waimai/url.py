from django.conf.urls import url,include
from django.contrib import admin
from waimai import views



urlpatterns = [
    url(r'^$', views.index,name='商城测试首页'),#类淘宝
    url(r'^weixin/$',views.weixin,name='微信接入'),
    url(r'^login/$',views.login,name='外卖登陆'),
    url(r'^regist/$',views.zhuce,name='外卖注册'),
    url(r'^fenlei/$',views.fenlei,name='美食分类'),
    # url(r'^list/$',views,name='全部商家'),
    # url(r'^shoppage/$',views,name='商家界面'),#购物车js脚本
    # url(r'^zhifu/$',views,name='收银台'),#结算界面
    # url(r'^user/$',views,name='用户中心'),#要有头像
    # url(r'^address/$',views,name='订餐地址'),#可以添加绑定默认地址
    # url(r'^/$',views,name= ''),
    #url(r'^/$',views,name= ''),


]