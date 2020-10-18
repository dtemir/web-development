from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


def IndexView(request):
    template_name = 'greeting/index.html'

    all_posts = Post.objects.filter(status=1).order_by('-created_on')
    project_posts = Post.objects.filter(status=1, category='Projects').order_by('-created_on')
    general_posts = Post.objects.filter(status=1, category='General').order_by('-created_on')
    college_posts = Post.objects.filter(status=1, category='College').order_by('-created_on')
    travelling_posts = Post.objects.filter(status=1, category='Travelling').order_by('-created_on')

    return render(request, template_name, {'post_list': all_posts,
                                           'projects_list': project_posts,
                                           'general_list': general_posts,
                                           'college_list': college_posts,
                                           'travelling_posts': travelling_posts,
                                           })


def ResumeView(request):
    template_name = 'greeting/resume.html'

    return render(request, template_name)


def ContactView(request):
    template_name = 'greeting/contact.html'

    return render(request, template_name)
