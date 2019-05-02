from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASECADE)
    content = models.CharField(max_length=200)
    tags = models.ManyToManyField(Tag, through='Categorize')
    success = models.BooleanField(defualt=False) 
    deadline = models.DateTimeField(null=True)

class Categorize(models.Model):
    tag  = models.ForeignKey(Tag, on_delete=models.CASECADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASECADE)

class DoneTodo(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASECADE)
    done_date = models.DateField(auto_now_add = True)