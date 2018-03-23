from django.shortcuts import render, get_object_or_404
from . import models
import markdown
# Create your views here.


# 主页视图函数
def index(request):
    post_list = models.Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html/', context={'post_list': post_list})


# 文章页视图函数
def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      # 'markdown.extensions.fenced_code',
                                      'markdown.extensions.toc'
                                  ])
    return render(request, 'blog/detail.html/', context={'post': post})


# 归档页视图函数
def archives(request, year, month):
    post_list = models.Post.objects.filter(created_time__year=year,
                                           created_time__month=month
                                           ).order_by('-created_time')
    return render(request,'blog/index.html', context={'post_list': post_list})