from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True)
    image = models.FileField(null=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        """
        Define la representación String de un Blog
        """

        return '{0}'.format(self.name)