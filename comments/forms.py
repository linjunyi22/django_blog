from django import forms
from .models import Comment


# 表单类
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']