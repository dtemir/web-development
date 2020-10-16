from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class IndexView(ListView):

    template_name = 'greeting/index.html'

    def __init__(self):
        queryset = Post.objects.filter(status=1).order_by('-created_on')
        context_object_name = 'post_list'
        self.queryset = queryset
        self.context_object_name = context_object_name
        super().__init__()


def ResumeView(request):

    template_name = 'greeting/resume.html'

    return render(request, template_name)


def ContactView(request):

    template_name = 'greeting/contact.html'

    return render(request, template_name)