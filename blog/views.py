from django.shortcuts import render, get_object_or_404
from . import models

from django.views.generic import ListView, DetailView
from comments.forms import CommentForm
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.db.models import Q

# 主页视图函数
# def index(request):
#     post_list = models.Post.objects.all()
#     return render(request, 'blog/index.html/', context={'post_list': post_list})

# 主页类视图方法
class IndexView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'
    paginate_by = 2


# 文章页视图函数
# def detail(request, pk):
#     post = get_object_or_404(models.Post, pk=pk)
#
#     # 阅读量
#     post.increase_views()
#
#     post.body = markdown.markdown(post.body,
#                                   extensions=[
#                                       'markdown.extensions.extra',
#                                       'markdown.extensions.codehilite',
#                                       # 'markdown.extensions.fenced_code',
#                                       'markdown.extensions.toc'
#                                   ])
#     form = CommentForm()
#     # 获取该文章下所有评论
#     comment_list = post.comment_set.all()
#
#     context = {'post': post,
#                'form': form,
#                'comment_list': comment_list
#                }
#
#     return render(request, 'blog/detail.html/', context=context)

class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = models.Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        post = super(PostDetailView, self).get_object(queryset=None)
        md = markdown.Markdown(extensions=[
            'markdown.extensions.extra',
            'markdown.extensions.codehilite',
            'markdown.extensions.toc',
            TocExtension(slugify=slugify)
        ])
        post.body = md.convert(post.body)
        post.toc = md.toc
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context

# 归档页视图函数
# def archives(request, year, month):
#     post_list = models.Post.objects.filter(created_time__year=year,
#                                            created_time__month=month
#                                            )
#     return render(request, 'blog/index.html/', context={'post_list': post_list})

# 归档页类视图函数
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

# 分类页类视图函数
class CategoryView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        cate = get_object_or_404(models.Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


# 标签视图函数
class TagView(ListView):
    model = models.Post
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        tag = get_object_or_404(models.Tag, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


# 搜索功能函数
def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = '请输入关键字'
        return render(request, 'blog/index.html', {'error_msg':error_msg})

    post_list = models.Post.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/index.html', {'error_msg': error_msg,
                                               'post_list': post_list})

