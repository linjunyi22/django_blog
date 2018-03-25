from django.db import models

# Create your models here.


class Comment(models.Model):
    '''
    评论数据表，用于存放评论人名称，email，url，评论内容，评论时间及对应的文章
    '''
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    url = models.URLField(blank=True)
    text = models.TextField()
    created_time = models.DateField(auto_now_add=True)  # 把 created_time 指定为当前时间

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
