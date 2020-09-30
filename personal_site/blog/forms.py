from .models import Comment, Post, Category
from django import forms


categories = Category.objects.all().values_list('name', 'name')
choices = [x for x in categories]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'slug', 'snippet', 'author', 'category', 'content', 'status',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '', 'id': 'views.author', 'type': 'hidden'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'header_image', 'slug', 'snippet', 'author', 'category', 'content', 'status')
