from django.contrib import admin
from product.models import Category, Course, Images, Course,Slider
from mptt.admin import MPTTModelAdmin,DraggableMPTTAdmin
from django.utils.html import format_html



class CategoryAdmin(MPTTModelAdmin):
    #fields = ['title', 'status'] sadece title ve status alır
    readonly_fields =('image_tag',)
    list_display=['title', 'status','image_tag']
    list_filter=['status']      #filtreleme ypar
    prepopulated_fields={'slug':('title',)}


class CourseImageInline(admin.TabularInline):
    model=Images
    extra=3

class CourseAdmin(admin.ModelAdmin):
    readonly_fields =('image_tag',)
    list_display=['title', 'status','price','category','image_tag']
    list_filter=['status','category']      #filtreleme ypar
    inlines=[CourseImageInline]
    prepopulated_fields={'slug':('title',)}
    


class ImagesAdmin(admin.ModelAdmin):
    readonly_fields =('image_tag',)
    list_display=['title', 'course','image_tag']
    list_filter=['course','title']      #filtreleme ypar


class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                Course,
                'category',
                'products_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 Course,
                 'category',
                 'products_count',
                 cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


class SliderAdmin(admin.ModelAdmin):
    list_display=['title','image_tag']
    


admin.site.register(Category,CategoryAdmin2)
admin.site.register(Course,CourseAdmin)
admin.site.register(Slider,SliderAdmin)
admin.site.register(Images,ImagesAdmin)

