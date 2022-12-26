
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from django.utils.crypto import get_random_string

from order.models import ShopCart,ShopCartForm
from product.models import Category
from home.models import Setting, UserProfile
from .models import OrderForm,Order,OrderProduct

def index(request):

    return HttpResponse('Order App')

@login_required(login_url='/login')
def addtocart(request,id):
    url=request.META.get('HTTP_REFERER')
    """
    if request.method=='POST':
        form=ShopCartForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=ShopCart()
            data.user.id=current_user.id
            data.product_id=id
            data.quantity=form.cleaned_data['quantity']
            data.save()

            messages.success(request,"Ürününüz Sepete Eklenmiştir")
            return HttpResponseRedirect(url)
    """
    if id:
        current_user=request.user
        data=ShopCart()
        data.user_id=current_user.id
        data.product_id=id
        data.quantity=1
        data.save()
        messages.success(request,"Ürününüz Sepete Eklenmiştir")
        return HttpResponseRedirect(url)
    request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()
    messages.warning(request,"Ürün Sepete Eklenemedi")
    return HttpResponseRedirect(url)

@login_required(login_url='/login')
def shopcart(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    current_user=request.user
    scart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in scart:
        total +=rs.product.price*rs.quantity
    context={'scart':scart,'category':category,'total':total,'setting':setting}
    request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()
    return render(request,'Shopcart_products.html',context)
    

@login_required(login_url='/login')
def deletefromcart(request,id):
    current_user=request.user
    ShopCart.objects.filter(id=id).delete()
    messages.success(request,"Ürün Sepetten Kaldırıldı")
    request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()
    return HttpResponseRedirect("/shopcart")


    
@login_required(login_url='/login')
def orderproduct(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    current_user=request.user
    scart=ShopCart.objects.filter(user_id=current_user.id)
    total=0
    for rs in scart:
        total+=rs.product.price*rs.quantity
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            data=Order()
            data.first_name=form.cleaned_data['first_name']
            data.last_name=form.cleaned_data['last_name']
            data.adress=form.cleaned_data['adress']
            data.city=form.cleaned_data['city']
            data.phone=form.cleaned_data['phone']
            data.user_id=current_user.id
            data.total=total
            data.ip=request.META.get('REMOTE_ADDR')
            ordercode=get_random_string(5).upper
            data.code=ordercode
            data.save()

            scart=ShopCart.objects.filter(user_id=current_user.id)
            for rs in scart:
                detail=OrderProduct()
                detail.order_id=data.id
                detail.product_id=rs.product_id
                detail.user_id=current_user.id
                detail.quantity=rs.quantity
                detail.price=rs.product.price
                detail.amount=rs.amount
                detail.save()
            ShopCart.objects.filter(user_id=current_user.id).delete()
            request.session['cart_items']=0
            messages.success(request,"Siparişiniz Alınmıştır")
            return render(request,'Order_completed.html',{'ordercode':ordercode,'category':category,'setting':setting})
        else:
            messages.warning(request,form.errors)
            return HttpResponseRedirect("/order/orderproduct")
    form=OrderForm()
    profile=UserProfile.objects.get(user_id=current_user.id)
    context={'scart':scart,'category':category,'setting':setting,'total':total,'form':form,'profile':profile}
    return render(request,'Order_Form.html',context)
