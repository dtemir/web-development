from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'slug', 'author', 'content', 'status')


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'slug', 'author', 'content', 'status')
