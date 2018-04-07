from django.db import models


class MsgBoard(models.Model):
    """
    留言板数据表,存储昵称、留言内容、留言时间
    """

    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)

    # 逆向排序
    class Meta:
        ordering = ['-created_time']

    def __str__(self):
        return self.name
