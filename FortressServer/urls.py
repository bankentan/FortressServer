"""FortressServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from MyFortress import views

urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', views.index),
    url('add_host/', views.add_host),
    url('get_host/', views.get_host),
    url('change_host/', views.change_host),
    url('del_host/', views.del_host),

]
