# Generated by Django 3.0.5 on 2020-05-01 17:18

import blogApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0010_auto_20200501_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, upload_to=blogApp.models.user_directory_path),
        ),
    ]