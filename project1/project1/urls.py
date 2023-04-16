"""project1 URL Configuration

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
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login/', views.gologin),
    path('register/',views.reg),
    path('user/',views.user),
    path('dictation/',views.dictation),
    path('test3/',views.test3),
    path('match/',views.match),
    path('comprehension/',views.comprehension),
    path('count/',views.count),
    path('currency/',views.currency),
    path('order/',views.order),
    path('solve/',views.solve),
    path('questionnaire/',views.questionnaire),
    path('fill/',views.fill),
    path('compare/',views.compare),
    path('result/',views.result),
]
