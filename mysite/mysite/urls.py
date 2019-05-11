# -*-coding:utf-8 -*-
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from learn import views as lean_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', lean_views.index, name='index'),
    # path('add/', lean_views.add, name='add'),
    path('add/<int:a>/<int:b>/', lean_views.add2, name='add2'),

    # url(r'^$', lean_views.index, name='home'),
    path('old/<int:a>/<int:b>/', lean_views.old_add2_redirect, name='old'),
]
