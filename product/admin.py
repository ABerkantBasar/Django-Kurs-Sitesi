from django.contrib import admin
from product.models import Category, Course

class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] sadece title ve status alır
    list_display=['title', 'status']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Category,CategoryAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display=['title', 'status','price','category','image']
    list_filter=['status','category']      #filtreleme ypar
admin.site.register(Course,CourseAdmin)
