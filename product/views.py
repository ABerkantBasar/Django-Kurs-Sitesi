from django.shortcuts import render
from django.contrib import messages
from product.models import CommentForm,Comment
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,HttpResponseRedirect

def index(request):
    text="Hi"
    context={'text':text}
    return render(request, 'indexproduct.html', context)




