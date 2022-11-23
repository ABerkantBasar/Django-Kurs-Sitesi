from django.contrib import admin
from product.models import Category, Course, Images


class CategoryAdmin(admin.ModelAdmin):
    #fields = ['title', 'status'] sadece title ve status alır
    readonly_fields =('image_tag',)
    list_display=['title', 'status','image_tag']
    list_filter=['status']      #filtreleme ypar
admin.site.register(Category,CategoryAdmin)

class CourseImageInline(admin.TabularInline):
    model=Images
    extra=3

class CourseAdmin(admin.ModelAdmin):
    readonly_fields =('image_tag',)
    list_display=['title', 'status','price','category','image_tag']
    list_filter=['status','category']      #filtreleme ypar
    inlines=[CourseImageInline]
    
admin.site.register(Course,CourseAdmin)

class ImagesAdmin(admin.ModelAdmin):
    readonly_fields =('image_tag',)
    list_display=['title', 'course','image_tag']
    list_filter=['course','title']      #filtreleme ypar
admin.site.register(Images,ImagesAdmin)


