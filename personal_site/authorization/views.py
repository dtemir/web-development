from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from . import forms
from django.urls import reverse_lazy


class UserRegisterView(generic.CreateView):
    form_class = forms.SignUpForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')
