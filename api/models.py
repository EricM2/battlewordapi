from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=19)
    hint = models.CharField(max_length=100)
    stage = models.IntegerField()

class Subscriber(models.Model):
    email = models.EmailField()
    date = models.DateTimeField()