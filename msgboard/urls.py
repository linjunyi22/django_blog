from django.urls import path
from . import views

# 留言板子路径
app_name = 'msgboard'

urlpatterns = [
    path(r'msgboard/', views.msg_board, name='msg_board'),
]
