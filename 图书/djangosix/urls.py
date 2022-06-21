"""djangosix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index,name='index_view'),
    url(r'^see_book', views.see_book,name='see_view'),
    url(r'^max_book', views.max_xiaoliang,name='max_view'),
    url(r'^create_book', views.create_book,name='create_view'),
    url(r'^caozuo_book', views.caozuo_book,name='caozuo_view'),
    url(r'^modify_book/(?P<update_id>\d+)/', views.modify_book,name='modify_view'),
    url(r'^drop_book//(?P<delect_id>\d+)/', views.drop_book,name='drop_view'),
    url((r'^aaa/'),views.test)
]
