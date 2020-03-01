from django.db import models

class NameTable(models.Model):
    name = models.CharField(max_length=30)
    nation = models.CharField(max_length=30)

    def __str__(self):
        return "<{0}>".format(self.name)