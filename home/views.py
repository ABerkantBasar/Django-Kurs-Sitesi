from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    text="Hello, world. You're at the home index.<br>merhaba<br>naber"
    context = {'text': text}
    return render(request, 'indexhome.html', context)