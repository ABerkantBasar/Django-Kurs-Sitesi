from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm,TextInput
from product.models import Course
from home.models import UserProfile

class ShopCart(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Course,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()

    def __str__(self):
        return self.product.title
    
    @property
    def amount(self):
        return (self.product.price)
    
    @property
    def price(self):
        return self.product.price

class ShopCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields=['quantity']

class Order(models.Model):
    STATUS=(
        ('New','Yeni'),
        ('Accepted','Kabul Edildi'),
        ('Preparing','Hazırlanıyor'),
        ('Completed','Tamamlandı'),
        ('Canceled','İptal Edildi')
    )

    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    code=models.CharField(max_length=5,editable=False)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    phone=models.CharField(blank=True,max_length=15)
    adress=models.CharField(blank=True,max_length=225)
    city=models.CharField(blank=True,max_length=40)
    country=models.CharField(blank=True,max_length=40)
    total=models.FloatField()
    status=models.CharField(max_length=18,choices=STATUS,default='Yeni')
    ip=models.CharField(blank=True,max_length=20)
    adminnote=models.CharField(blank=True,max_length=200)

    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name

class OrderForm(ModelForm):
    class Meta:
        model=Order
        fields=['first_name','last_name','adress','phone','city','country']

class OrderProduct(models.Model):
    STATUS=(
        ('New','Yeni'),
        ('Accepted','Kabul Edildi'),
        ('Canceled','İptal Edildi')
    )
    order=models.ForeignKey(Order,on_delete=models.SET_NULL,null=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Course,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    price=models.IntegerField()
    amount=models.IntegerField()
    
    
    status=models.CharField(max_length=18,choices=STATUS,default='Yeni')
    crate_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.product.title