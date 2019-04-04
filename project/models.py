from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    qualifications = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='images')


def __str__(self):
    return self.name


