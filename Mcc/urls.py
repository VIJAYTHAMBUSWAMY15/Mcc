"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from Mcc import views

app_name = 'Mcc'
urlpatterns = [
    
     path('about.html', views.about, name='about.html'),
     path('appointment.html', views.appointment, name='appointment.html'),
     path('blog_details.html', views.blog_details, name='blog_details.html'),
     path('blog.html', views.blog, name='blog'),
     path('contact.html', views.contact, name='contact.html'),
     path('gallery.html', views.gallery, name='gallery.html'),
     path('index.html', views.index, name='index.html'),
     path('service.html', views.service, name='service.html'),
     path('team.html', views.team, name='team.html'),
     path('info', views.info, name = 'info'),
    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login_reg'),
    path('logout', views.logoutuser, name = 'logout'),
    path('product', views.product, name='product'),
    path('products', views.products, name='products'),
    path('order/<int:id>', views.order, name='order'),
    path('kart', views.kart  , name='kart'),
    path('login',views.login,name='login'),


   
]


