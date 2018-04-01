from django.contrib import admin
from .models import Post, Category, Tag


# 增添详细信息
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']

# 注册数据表
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
