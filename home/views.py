from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactFormMessage, ContactFormu, Comment, CommentForm, UserProfile, FAQ
from django.contrib import messages
from product.models import Course,Category,Images,Slider
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .forms import SearchForm
from order.views import ShopCart, OrderProduct


def index(request):
    slider=Slider.objects.all()
    current_user=request.user
    category=Category.objects.all
    setting=Setting.objects.get(pk=1)
    sliderdata=Course.objects.all()[:10]
    selected_category=Category.objects.all()
    course_data=Course.objects.all().order_by('?')
    course_data_last=Course.objects.all().order_by('-id')[0:4]

    request.session['cart_items']=ShopCart.objects.filter(user_id=current_user.id).count()

    context = {'setting': setting, 
                'page':'home',
                'sliderdata':sliderdata,
                'category':category,
                'selected_category':selected_category,
                'course_data':course_data,
                'course_data_last':course_data_last,
                'slider':slider,}

    return render(request, 'indexhome.html', context)

def about(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    context = {'setting': setting, 'page':'about','category':category}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email=form.cleaned_data['email']
            data.phone=form.cleaned_data['phone']
            data.subject=form.cleaned_data['subject']
            data.message=form.cleaned_data['message']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request,"Mesajınız Başarı İle Gönderilmiştir")
            return HttpResponseRedirect('/contact')
    category=Category.objects.all()
    setting= Setting.objects.get(pk=1)
    form= ContactFormu()
    context={'setting':setting,'form':form,'category':category}
    return render(request,'contact.html',context)

def faq(request):
    faq=FAQ.objects.all().order_by('id')
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    context = {'setting': setting,'category':category,'faq':faq}
    return render(request, 'faq.html', context)

def product(request):
    course_data_last=Course.objects.all().order_by('-id')[0:4]
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    sliderdata=Course.objects.all()[:10]
    course_data=Course.objects.all().order_by('?')
    context = {'setting': setting, 'sliderdata':sliderdata,'category':category,'course_data_last':course_data_last,'course_data':course_data}
    return render(request, 'product.html', context)

def category_products(request,id,slug):
    category=Category.objects.all
    sliderdata=Course.objects.all()[:10]
    setting=Setting.objects.get(pk=1)
    selected_category=Category.objects.filter(pk=id)
    product=Course.objects.filter(category_id=id)
    context={'setting': setting,'product':product,'category':category,'sliderdata':sliderdata,'selected_category':selected_category}
    return render(request,'category.html',context)

def product_details(request,id,slug):
    if request.user.id is not None:
        orders=OrderProduct.objects.filter(user_id=request.user.id )
        user=UserProfile.objects.get(user_id=request.user.id)
        comment=Comment.objects.filter(product_id=id,status='True')
        setting=Setting.objects.get(pk=1)
        category=Category.objects.all()
        product=Course.objects.filter(pk=id)
        context={'setting':setting ,'product':product, 'category':category, 'user':user, 'slug':slug,'comment':comment}
        return render(request,'product_detail.html',context)
    else:
        comment=Comment.objects.filter(product_id=id,status='True')
        setting=Setting.objects.get(pk=1)
        category=Category.objects.all()
        product=Course.objects.filter(pk=id)
        context={'setting':setting ,'product':product, 'category':category, 'slug':slug,'comment':comment}
        return render(request,'product_detail.html',context)


@login_required(login_url='/login')
def addcomment(request,id):
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            current_user=request.user

            data=Comment()
            data.user_id=current_user.id
            data.product_id=id
            data.subject=form.cleaned_data['subject']
            data.comment=form.cleaned_data['comment']
            #data.rate=form.cleaned_data['rate']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request,"Yorumunuz Başarı ile Gönderilmiştir")
            url=request.META.get('HTTP_REFERER')
            return HttpResponseRedirect(url)
    return HttpResponse("Kaydetme İşlemi Gerçekleştirilemedi")



def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/home')

def login_view(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/home')
            ...
        else:
            messages.error=(request,"Giriş Yapma İşlemi Gerçekleştirilemedi")
            return HttpResponseRedirect('/login')
    
    category=Category.objects.all()
    setting=Setting.objects.get(pk=1)
    context={'category':category,'setting':setting,}
    return render(request,'login.html',context)

def product_search(request):
    if request.method=='POST':
        form=SearchForm(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query=form.cleaned_data['query']
            product=Course.objects.filter(title__icontains=query)
            setting=Setting.objects.get(pk=1)
            context={'category':category,'setting':setting,'product':product,}
            return render(request,'product_search.html',context)
            
    return HttpResponseRedirect('/home')
    
    
    
    