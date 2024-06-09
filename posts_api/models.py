from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=256)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, related_name='posts',on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username + ': ' + self.title