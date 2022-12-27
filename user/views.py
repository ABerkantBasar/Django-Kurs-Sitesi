
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.models import Course,Category,Images
from home.models import Setting, UserProfile, UserProfileForm, Comment
from order.models import OrderProduct
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    user=UserProfile.objects.get(user_id=request.user.id)
    category=Category.objects.all
    setting=Setting.objects.get(pk=1)
    selected_category=Category.objects.all()
    course_data=Course.objects.all().order_by('?')
    

    context = {'setting': setting, 
                'category':category,
                'selected_category':selected_category,
                'course_data':course_data,
                'user':user,
                }
    return render(request,'user_profile.html',context)

@login_required(login_url='/login')
def orders(request):
    current_user=request.user
    orders=OrderProduct.objects.filter(user_id=current_user.id)
    category=Category.objects.all
    setting=Setting.objects.get(pk=1)
    selected_category=Category.objects.all()
    course_data=Course.objects.all().order_by('?')
    
    context = {'setting': setting, 
                'category':category,
                'selected_category':selected_category,
                'course_data':course_data,
                'orders':orders,
                }
    return render(request,'orders.html',context)

@login_required(login_url='/login')

def order_detail(request,id):
    current_user=request.user
    orders=OrderProduct.objects.filter(user_id=current_user.id)
    user=UserProfile.objects.get(user_id=request.user.id)
    comment=Comment.objects.filter(product_id=id,status='True')
    setting=Setting.objects.get(pk=1)
    selected_category=Category.objects.all()
    course_data=Course.objects.all().order_by('?')
    category=Category.objects.all()
    product=Course.objects.filter(pk=id)
    
    context={
        'orders':orders,
        'user':user,
        'comment':comment,
        'setting':setting,
        'selected_category':selected_category,
        'course_data':course_data,
        'category':category,
        'product':product,
    }
    return render(request,'order_detail.html',context)
    
