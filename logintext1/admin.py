from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from logintext1.models import *#,UploadAdmin

admin.site.register(Upload,UploadAdmin)
admin.site.register(User)