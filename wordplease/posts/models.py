from django.contrib.auth.models import User
from django.db import models

from blogs.models import Blog
from themes.models import Theme


class Post(models.Model):


    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    themes = models.ManyToManyField(Theme)
    title = models.CharField(max_length=100)
    creation_date = models.DateTimeField(auto_now_add=True)
    intro = models.TextField(null=True)
    text = models.TextField(null=True)
    image = models.FileField(null=True)
    active = models.BooleanField(default=True)



    def __str__(self):
        """
        Define la representación String de un Post
        """

        return '{0}'.format(self.title)