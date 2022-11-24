from django.contrib import admin
from home.models import Setting

class SettingAdmin(admin.ModelAdmin):
    list_display=['title', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Setting,SettingAdmin)
