"""cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('greet/<str:name>/',greet),
    path('post/<int:post_id>/',post_page),
    path('allposts/',all_posts),
    path('create/',create_post),
    path('delete/<int:post_id>/',delete_post),
    path('edit/<int:post_id>/',edit_post),
    path('signup/',signup),
    path('signin/',signin),
    path('signout/',signout), 
]
