from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField
from mptt.models import MPTTModel, TreeForeignKey
from django.forms import ModelForm, TextInput, Textarea
from django.contrib.auth.models import User
from django.urls import reverse




class Category(MPTTModel):
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    )
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    keywords=models.CharField(max_length=255)
    image=models.ImageField(blank=True,upload_to='images/')
    status=models.CharField(max_length=10,choices=STATUS)

    slug=models.SlugField(null=False,unique=True)     #id gibi ama metin 

    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    parent=TreeForeignKey('self',on_delete=models.CASCADE,null=True,blank=True,related_name='children')

    class MPTTMeta:
        #level_attr = 'mptt_level'
        order_insertion_by=['title']
    def __str__(self):
        full_path =[self.title]
        k=self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return ' / '.join(full_path[::-1])    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    def get_absolute_url(self):
        return reverse('Category',kwargs={'slug':self.slug})


class Course(models.Model):
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    )
    category=models.ForeignKey(Category,on_delete=models.CASCADE)     #relation with category
    title=models.CharField(max_length=150)
    description=models.CharField(max_length=255)
    keywords=models.CharField(max_length=255)
    slug=models.SlugField(null=False,unique=True)
    image=models.ImageField(upload_to='images/')
    video=models.FileField(upload_to='videos/')
    price=models.FloatField()
    status=models.CharField(max_length=10,choices=STATUS)
    detail=RichTextUploadingField()
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

    def get_absolute_url(self):
        return reverse('Course',kwargs={'slug':self.slug})


class Images(models.Model):
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    title=models.CharField(max_length=150)
    image=models.ImageField(blank=True,upload_to='images/')
    def __str__(self):
        return self.title
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))



class Slider(models.Model):
    title=models.CharField(max_length=150)
    image=models.ImageField(blank=True,upload_to='images/')
    text1=models.TextField()
    text2=models.TextField()
    text3=models.TextField()
    def __str__(self):
        return self.title           #geri dönüş
    
    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    
    


        
    