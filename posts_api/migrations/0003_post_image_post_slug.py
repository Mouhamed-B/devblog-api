# Generated by Django 4.2.13 on 2024-07-14 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts_api', '0002_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]