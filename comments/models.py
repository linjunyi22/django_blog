from django.db import models


class Comment(models.Model):
    """
    评论数据表，用于存放名称，评论内容，评论时间及对应的文章
    """
    name = models.CharField(max_length=100)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)  # 把 created_time 指定为当前时间

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
