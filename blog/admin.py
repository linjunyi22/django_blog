from django.contrib import admin
from .models import Post, Category, Tag

# Register your models here.

'''
username:linjunyi22
email:lin@admin.com
password:ljy121800
'''

# 注册models 中的三个数据表
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
