from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Description(models.Model):
    text = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

class Experience(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = RichTextField(blank=True, null=True, config_name='default')
    period = models.DateField(auto_now_add=False, auto_now=False, blank=True)