"""
URL configuration for poetry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from verse.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vers/', verse_list, name='verse_list'),
    path('', poem_list, name='poem_list'),
    path('like/<int:poem_id>/', like_poem, name='like_poem'),
    path('dislike/<int:poem_id>/', dislike_poem, name='dislike_poem'),
]
