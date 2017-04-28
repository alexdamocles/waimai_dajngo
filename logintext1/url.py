from django.conf.urls import  url
from logintext1 import views


urlpatterns = (
    url(r'^$', views.index, name='陕服外卖'),
    url(r'^login/$',views.login,name = '登陆2'),
    url(r'^regist/$',views.regist,name = '注册'),
    url(r'^user/$',views.user,name = '个人中心'),
    url(r'^logout/$',views.logout,name = '登出'),
    url(r'^upload/$',views.upload,name='上传测试'),
    url(r'^add/$',views.add,name='收货地址列表'),
    url(r'^ziliao/$',views.ziliao,name='个人资料'),
    url(r'^createadd/$',views.create_add,name='添加收货地址'),

    #url(r'^')
)