# Generated by Django 3.1.1 on 2021-01-06 03:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('greeting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='description',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
