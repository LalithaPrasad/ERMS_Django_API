"""api_django_erms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app_django import admin_views, employee_views
from rest_framework import routers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_admin/', admin_views.create_admin),
    path('get_token/', admin_views.fetch_token),
    path('add_employee/', employee_views.add_employee),
    path('delete_employee/', employee_views.delete_employee),
    path('modify_employee/', employee_views.modify_employee),
    path('display_employees/', employee_views.display_employees),
]
