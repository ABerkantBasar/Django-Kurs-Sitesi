from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from home.models import Setting, ContactFormMessage, ContactFormu
from django.contrib import messages
from product.models import Course

def index(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Course.objects.all()[:10]
    context = {'setting': setting, 'page':'home','sliderdata':sliderdata}
    return render(request, 'indexhome.html', context)

def about(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'about'}
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
    
    setting= Setting.objects.get(pk=1)
    form= ContactFormu()
    context={'setting':setting,'form':form}
    return render(request,'contact.html',context)
 

def blog(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'blog'}
    return render(request, 'blog.html', context)

def faq(request):
    setting=Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'faq'}
    return render(request, 'faq.html', context)

def product(request):
    setting=Setting.objects.get(pk=1)
    sliderdata=Course.objects.all()[:10]
    context = {'setting': setting, 'page':'product','sliderdata':sliderdata}
    return render(request, 'product.html', context)