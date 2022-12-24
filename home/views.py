from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactFormMessage, ContactFormu, Comment, CommentForm
from django.contrib import messages
from product.models import Course,Category,Images
from django.contrib.auth.decorators import login_required


def index(request):
    category=Category.objects.all
    setting=Setting.objects.get(pk=1)
    sliderdata=Course.objects.all()[:10]
    selected_category=Category.objects.all()
    course_data=Course.objects.all().order_by('?')

    context = {'setting': setting, 
                'page':'home',
                'sliderdata':sliderdata,
                'category':category,
                'selected_category':selected_category,
                'course_data':course_data}

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
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    context = {'setting': setting, 'page':'faq','category':category}
    return render(request, 'faq.html', context)

def product(request):
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    sliderdata=Course.objects.all()[:10]
    course_data=Course.objects.all().order_by('?')
    context = {'setting': setting, 'sliderdata':sliderdata,'category':category,'course_data':course_data}
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
    comment=Comment.objects.filter(product_id=id,status='True')
    setting=Setting.objects.get(pk=1)
    category=Category.objects.all()
    product=Course.objects.filter(pk=id)
    images=Images.objects.filter(course_id=id)
    #comments=Comment.objects.filter(policlinic_id=id,status='True')
    context={'setting':setting ,'product':product, 'category':category, 'images':images, 'slug':slug,'images':images,'comment':comment}
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