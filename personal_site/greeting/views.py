from django.shortcuts import render


def IndexView(request):

    template_name = 'greeting/index.html'

    return render(request, template_name)


def ResumeView(request):

    template_name = 'greeting/resume.html'

    return render(request, template_name)


def ContactView(request):

    template_name = 'greeting/contact.html'

    return render(request, template_name)