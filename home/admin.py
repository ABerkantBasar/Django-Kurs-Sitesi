from django.contrib import admin
from home.models import Setting, ContactFormMessage

class SettingAdmin(admin.ModelAdmin):
    list_display=['title', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Setting,SettingAdmin)

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display=['name','email','subject', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(ContactFormMessage,ContactFormMessageAdmin)
