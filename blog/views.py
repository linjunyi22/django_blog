from django.shortcuts import render, get_object_or_404
from . import models

from django.views.generic import ListView
from comments.forms import CommentForm
import markdown

# Create your views here.


# 主页视图函数
# def index(request):
#     post_list = models.Post.objects.all()
#     return render(request, 'blog/index.html/', context={'post_list': post_list})

# 类视图方法
class IndexView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'


# 文章页视图函数
def detail(request, pk):
    post = get_object_or_404(models.Post, pk=pk)

    # 阅读量
    post.increase_views()

    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      # 'markdown.extensions.fenced_code',
                                      'markdown.extensions.toc'
                                  ])
    form = CommentForm()
    # 获取该文章下所有评论
    comment_list = post.comment_set.all()

    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }

    return render(request, 'blog/detail.html/', context=context)


# 归档页视图函数
# def archives(request, year, month):
#     post_list = models.Post.objects.filter(created_time__year=year,
#                                            created_time__month=month
#                                            )
#     return render(request, 'blog/index.html/', context={'post_list': post_list})

class ArchivesView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView, self).get_queryset().filter(created_time__year=year,
                                                               created_time__month=month)



# 分类页视图函数
# def category(request, pk):
#     cate = get_object_or_404(models.Category, pk=pk)  # 根据pk先将分类表里的记录查出来
#     post_list = models.Post.objects.filter(category=cate)  # 根据分类名查记录
#     return render(request, 'blog/index.html/', context={'post_list': post_list})

class CategoryView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(models.Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)

