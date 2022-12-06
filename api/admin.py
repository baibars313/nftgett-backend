from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
# Register your models here.


admin.site.register(Items)
admin.site.register(Userr)
