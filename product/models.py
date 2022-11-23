from django.db import models
from django.utils.safestring import mark_safe

class Category(models.Model):
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    )
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    keywords=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)

    slug=models.SlugField()     #id gibi ama metin 
    parent=models.ForeignKey('self',blank=True,null=True,related_name='lesson',on_delete=models.CASCADE)

    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title            #geri dönüş
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
class Course(models.Model):
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)     #relation with category
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    keywords=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    price=models.FloatField()
    detail=models.TextField()              #RichTextUploadingField()
    status=models.CharField(max_length=10,choices=STATUS)

    #slug=models.SlugField()     #id gibi ama metin 
    #parent=models.ForeignKey('self',blank=True,null=True,related_name='lesson',on_delete=models.CASCADE)

    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title            #geri dönüş
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'
    
    #def get_cat_list(self):
        #k=self.category
        #breadcrumb=["dummy"]
        #while k is not None:
            #breadcrumb.append(k.slug)
            #k=k.parent

class Images(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    