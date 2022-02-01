
from email.policy import default
from platform import node
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='defaul.jpg', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def limitBody(self):
        return self.body[0:50] + ' ...'
