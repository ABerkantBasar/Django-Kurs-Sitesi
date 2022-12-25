
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from product.models import Course,Category,Images
from home.models import Setting, UserProfile, UserProfileForm
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
