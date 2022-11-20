from django.contrib import admin
from product.models import Category

class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] sadece title ve status alır
    list_display=['title', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Category,CategoryAdmin)
