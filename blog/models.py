from django.db import models
# 导入 django 内置的 User 表
from django.contrib.auth.models import User
# 导入 reverse 函数
from django.urls import reverse
from django.utils.html import strip_tags

# Create your models here.


class Category(models.Model):
    '''
    目录表
    数据表模型继承自 models.Model 类
    存放目录列表，定义一个 CharField 的数据类型
    '''

    # 分类名 默认情况下 CharField 要求我们必须存入数据，否则就会报错
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name  # 返回目录表字段名，使得使用shell 和 admin时更方便


class Tag(models.Model):
    '''
    标签表，表中放置每篇文章对应的标签名
    '''

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name # 返回标签表字段名


class Post(models.Model):
    '''
    文章表
    存放文章对应的标题，正文，创建时间，修改时间，文章摘要，文章作者和文章对应的标签和分类
    因此需要创建8个对应的字段，其中标签,分类,作者用于外键关联
    '''

    # 文章标题
    title = models.CharField(max_length=100)

    # 文章正文，文本类数据使用 TextField 数据类型
    body = models.TextField()

    # 文章创建时间和修改时间，时间使用 DateTimeField 类型
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 文章摘要，可以为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 文章作者
    # django.contrib.auth 是 Django 内置的应用，专门用于处理网站用户的注册、登录等流程，User 是 Django 为我们已经写好的用户模型。
    # 这里通过 ForeignKey 把文章和 User 关联了起来。
    # 因为一篇文章只能有一个作者，而一个作者可能会写多篇文章，因此这是一对多的关联关系。
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # 一篇文章只能对应一个分类，但是一个分类下可以有多篇文章，因此使用 ForeignKey，即一对多的关联关系。
    # 而对于标签来说，一篇文章可以有多个标签，同一个标签下也可能有多篇文章，因此使用 ManyToManyField，表明这是多对多的关联关系。
    # 同时文章可以没有标签，因此为标签 tags 指定了 blank=True。
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # 逆向解析 url 获取 pk 参数，传递给 detail 视图函数处理并渲染页面
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title  # 返回文章名称

    # 指定排序
    class Meta:
        ordering = ['-created_time']

