from django.contrib import admin

# Register your models here.
from bolgtext1.models import BolgPost,BolgPostAdmin,Richang,richnagAdmin,Movie,MovieAdmin

admin.site.register(BolgPost,BolgPostAdmin)
admin.site.register(Richang,richnagAdmin)#注册模块到admin后台
admin.site.register(Movie,MovieAdmin)#注册模块到admin后台