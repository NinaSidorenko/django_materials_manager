from django.db import models
from django.contrib.auth.models import User
class Genre(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,
    null=True, blank=True)
    page = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class Article(models.Model):
    title = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,
    null=True, blank=True)
    page = models.IntegerField()
    
    def __str__(self):
        return self.link