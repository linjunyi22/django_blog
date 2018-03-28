# 自定义模板标签

from ..models import Post, Category, Tag
from django import template
from django.db.models.aggregates import Count

register = template.Library()


# 最新文档模板标签
@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


# 归档模板标签
@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')


# 分类模板标签
@register.simple_tag
def get_categories():
    # return Category.objects.all()
    # count 接收一个和 Category 相关联的模型参数名（此处是 post，通过外键关联），然后统计 Category 记录的集合中每条记录下与之关联的 Post 记录的行数
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

# 标签云模板标签
@register.simple_tag
def get_tags():
    # return Tag.objects.all()
    # Count 内参数为与 Tag 有关的表的字段
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)