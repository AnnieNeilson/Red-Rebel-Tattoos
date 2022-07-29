# Generated by Django 3.2.14 on 2022-07-29 20:35

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artwork', '0010_auto_20220726_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='preview_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
    ]