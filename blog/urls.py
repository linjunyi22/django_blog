# blog 应用子路径


from django.urls import path
from .feeds import AllPostsRssFeed

from . import views

app_name = 'blog'

urlpatterns = [
    path(r'index/', views.IndexView.as_view(), name='index'),
    path(r'post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path(r'archives/<int:year>/<int:month>', views.ArchivesView.as_view(), name='archives'),
    path(r'category/<int:pk>/', views.CategoryView.as_view(), name='category'),
    path(r'tag/<int:pk>/', views.TagView.as_view(), name='tag'),
    path(r'all/rss/', AllPostsRssFeed(), name='rss'),
    path(r'search/', views.search, name='search'),
    path(r'about/', views.about, name='about')
]