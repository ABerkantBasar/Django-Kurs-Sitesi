from django.shortcuts import render

def index(request):
    text="Hi"
    context={'text':text}
    return render(request, 'indexproduct.html', context)

