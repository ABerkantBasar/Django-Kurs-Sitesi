"""Proje1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from home import views


urlpatterns = [
    path('', include('home.urls')),               #hiçbirşey yazılmadığı zaman home a git
    path('home/', include('home.urls')),          #home/ yazıldığı zaman home a git
    #path('product/', include('product.urls')),    #product/ yazıldığı zaman product a git
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('faq/', views.faq, name='faq'),
    path('product/', views.product, name='product'),
    path('admin/', admin.site.urls),
    path('category/<int:id>/<slug:slug>/', views.category_products, name='category_products'),
    path('product/<int:id>/<slug:slug>/', views.product_details, name='product_detail'),
    path('product/addcomment/<int:id>/', views.addcomment, name='addcomment'),
]

if settings.DEBUG: #new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


