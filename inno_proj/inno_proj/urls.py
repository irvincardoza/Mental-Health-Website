"""inno_proj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from inno_app import views
from django.conf.urls import include
urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',include('inno_app.urls')),

    # path('contact/',views.contact,name='contact'),
    # path('display/',views.display, name='display'),
    # path('article1/',views.article1,name='article1'),
    # path('article2/',views.article2,name='article2'),
    # path('article3/',views.article3,name='article3'),
    # path('article4/',views.article4,name='article4'),
    # path('article5/',views.article5,name='article5'),
    # path('story/',views.story,name='story'),
    # path('info/',views.info,name='info'),
    # path('upload/',views.upload,name='upload'),


]
