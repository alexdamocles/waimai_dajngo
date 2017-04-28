"""djangot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from bolgtext1 import views as views1
from djangot import settings

from bolgtext1 import views

from logintext1 import views as views2

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views1.index,name='商城测试'),
    #url(r'^logintext1/',views2.login),
    url(r'^hhh/',include('waimai.url'),name='陕服外卖'),
    url(r'^bolg/',include('bolgtext1.url'),name='博客测试'),
    url(r'^t/',include('logintext1.url'),name='测试'),
    #url(r'^favicon.ico/$',views.tubiao,name='tubiao')
    #url(r"^uploads/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
]
