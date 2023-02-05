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

# path('base url 다음에 오는 주소', include('위임할 파일'))
urlpatterns = [
    path('admin/', admin.site.urls), # django의 관리자 페이지
    path('', include('practiceapp.urls')) # admin이 아닌 다른 경로로 접속하면 practiceapp의 urls로 위임
]
