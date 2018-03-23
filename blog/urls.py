# blog 应用子路径

from django.contrib import admin
from django.urls import path

from . import views

app_name = 'blog'

urlpatterns = [
    path(r'index/', views.index, name='index'),
    path(r'post/<int:pk>/', views.detail, name='detail'),
    path(r'archives/<int:year>/<int:month>', views.archives, name='archives')
]