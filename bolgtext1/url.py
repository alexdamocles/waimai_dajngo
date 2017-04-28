from django.conf.urls import  url
from bolgtext1 import views

urlpatterns = [

    url(r'^$', views.mybolg,name='技术'),
    #url(r'^logintext1/',views2.login),

    url(r'^richang/$',views.richang,name='日常'),

]
