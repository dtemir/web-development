from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Description(models.Model):
    text = RichTextField(blank=True, null=True)
