from turtle import title
from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length= 50)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def limitBody(self):
        return self.body[0:50] + ' ...'
