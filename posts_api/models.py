from typing import Iterable
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    image = models.ImageField(null=True,blank=True)
    description = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + ': ' + self.title
    
    def save(self, *args,**kwargs):
        self.slug = slugify(self.title+str(self.pk))
        super().save(*args, **kwargs)
