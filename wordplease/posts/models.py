from datetime import datetime

import django
from django.contrib.auth.models import User
from django.db import models


from blogs.models import Blog
from themes.models import Theme

def get_default_date():
  return datetime.now().date()


class Post(models.Model):


    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    themes = models.ManyToManyField(Theme)
    publication_date = models.DateField(default=get_default_date())
    creation_date = models.DateField(auto_now_add=True)
    intro = models.TextField(null=True)
    text = models.TextField(null=True)
    image = models.FileField(null=True)
    active = models.BooleanField(default=True)



    def __str__(self):
        """
        Define la representación String de un Post
        """

        return '{0}'.format(self.title)