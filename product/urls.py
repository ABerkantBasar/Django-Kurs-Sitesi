from django.urls import path

from . import views

urlpatterns = [
    # ex: /product/
    path('', views.index, name='index'),
    
  

]