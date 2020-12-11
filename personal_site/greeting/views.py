from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


def IndexView(request):
    template_name = 'greeting/index.html'

    posts = Post.objects.filter(status=1).order_by('-created_on')

    return render(request, template_name, {
                                           'posts': posts,
                                           })


def ResumeView(request):
    template_name = 'greeting/resume.html'

    return render(request, template_name)


def ContactView(request):
    template_name = 'greeting/contact.html'

    return render(request, template_name)
