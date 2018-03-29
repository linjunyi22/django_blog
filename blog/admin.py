from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 注册models 中的三个数据表
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
