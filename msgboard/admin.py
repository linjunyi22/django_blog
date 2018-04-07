from django.contrib import admin
from .models import MsgBoard


class MsgBoardAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'created_time']

# 注册留言模型
admin.site.register(MsgBoard, MsgBoardAdmin)
