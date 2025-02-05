from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body", "status"]
        widgets = {
            "body": CKEditor5Widget(
                attrs={"class": "django_ckeditor_5"}, config_name="default"
            )
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
