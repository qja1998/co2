"""practice URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from practiceapp import views

urlpatterns = [
    path('', views.index), # path가 아니라 함수일 경우 include 없이
    path('create/', views.create),
    path('read/<id>/', views.read), # 바뀔 수 있는 값은 <>안에 이름을 넣어 받을 수 있음
    path('delete/', views.delete),
]
