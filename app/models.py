from django.db import models

class Artist(models.Model):
    username = models.CharField(max_length=30)
    email = models.TextField(max_length=50)
    login = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    choices = models.CharField(max_length=20, blank=True, null=True, choices =[('1', 'eplaysan'), ('2', "barbir eplaysan")])

class Album(models.Model):
    name = models.CharField( max_length=30, blank=True, null=True)
    copy = models.ManyToManyField('Artist')

class Song(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    copy = models.ForeignKey('Album', on_delete=models.CASCADE)
