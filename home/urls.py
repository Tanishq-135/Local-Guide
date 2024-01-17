"""
URL configuration for localguide project.

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
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
  path('', views.index, name='home'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),        
  path('food/', views.food, name='food'),        
  path('shopping/', views.shopping, name='shopping'),        
  path('services/', views.services, name='services'),        
  path('outdoors/', views.outdoors, name='outdoors'),        
  path('religious/', views.religious, name='religious'),              
  path('things/', views.things, name='things'),        
  path('season/', views.season, name='season'),        
  path('food_output/', views.food_output, name='food_output'),
  path('shopping_output/', views.shopping_output, name='shopping_output'),
  path('services_output/', views.services_output, name='services_output'),
  path('sign_up/', views.sign_up, name='sign_up'),
  path('sign_in/', views.sign_in, name='sign_in'),
  path('logout/', views.logout, name='logout'),
]
