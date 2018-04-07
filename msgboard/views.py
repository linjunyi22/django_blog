from django.shortcuts import render, get_object_or_404, redirect
from .models import MsgBoard


# 留言板函数
def msg_board(requests):
    # 获取全部留言内容待渲染
    messages = MsgBoard.objects.all()

    # 若提交了表单则写到数据库然后重新渲染，否则直接渲染页面
    if requests.method == 'POST':

        name = requests.POST.get('name')
        text = requests.POST.get('message')
        content = MsgBoard(name=name, text=text)
        content.save()
        messages = MsgBoard.objects.all()
        return render(requests, 'blog/msgboard.html', {'messages': messages})

    return render(requests, 'blog/msgboard.html/', {'messages': messages})
