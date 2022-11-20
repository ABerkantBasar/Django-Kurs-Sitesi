from django.db import models

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
