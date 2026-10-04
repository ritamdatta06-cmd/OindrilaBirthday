"""
URL configuration for OindrilaBirthday project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from OindrilaBirthday import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.landing_page, name='landing_page'),
    path('birthday/', views.birthday, name='birthday'),
    path('cakecut/', views.cakecut, name='cakecut'),
    path('thank_you/', views.thank_you, name='thank_you'),
    path('final/', views.final, name='final')
]
