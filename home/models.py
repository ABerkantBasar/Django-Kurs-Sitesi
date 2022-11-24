from django.db import models
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import  RichTextUploadingField


class Setting(models.Model): 
    STATUS=(
        ('True','Evet'),
        ('False','Hayir'),
    ) 
    title=models.CharField(max_length=150) 
    description=models.CharField(blank=True,max_length=255)
    keywords=models.CharField(blank=True,max_length=255)
    company=models.CharField(max_length=50)
    icon=models.ImageField(blank=True,upload_to='images/')
    logo=models.ImageField(blank=True,upload_to='images/')

    adress=models.CharField(blank=True,max_length=255)
    phone=models.CharField(blank=True,max_length=15)
    fax=models.CharField(blank=True,max_length=15)
    email=models.CharField(blank=True,max_length=50)

    smtpserver=models.CharField(max_length=20)
    smtpemail=models.CharField(max_length=20)
    smtppassword=models.CharField(max_length=10)
    smtpport=models.CharField(max_length=5)

    facebook=models.CharField(blank=True,max_length=150)
    pinterest=models.CharField(blank=True,max_length=150)
    instagram=models.CharField(blank=True,max_length=50)
    twitter=models.CharField(blank=True,max_length=50)
    telegram=models.CharField(blank=True,max_length=50)

    aboutus=RichTextUploadingField(blank=True,)
    contact=RichTextUploadingField(blank=True,)
    references=RichTextUploadingField(blank=True,)
    
    status=models.CharField(max_length=10,choices=STATUS)
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title  
      
    