from django.db import models

class Theme(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        """
        Define la representación String de un tema
        """

        return '{0}'.format(self.name)