from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post
from .models import Description, Experience


def IndexView(request):
    template_name = 'greeting/index.html'

    description = Description.objects.order_by('-created_on')[0]
    posts = Post.objects.filter(status=1).order_by('-created_on')
    experiences = Experience.objects.order_by('-period')


    return render(request, template_name, {'posts': posts,
                                           'description': description,
                                           'experiences': experiences})


def ResumeView(request):
    template_name = 'greeting/resume.html'

    return render(request, template_name)


def ContactView(request):
    template_name = 'greeting/contact.html'

    return render(request, template_name)


def error_404_view(request, exception):
    """
    404 Error Handling Page
    """
    template_name = 'greeting/404.html'

    posts = Post.objects.filter(status=1).order_by('-created_on')

    return render(request, template_name, {'posts': posts})
