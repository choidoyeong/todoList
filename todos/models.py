from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=200)

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASECADE)
    todo_title = models.CharField(max_length=200)
    todo_content = models.TextField()
    tags = models.ManyToManyField(Tag, through='Categorize')
    success = models.BooleanField(defualt=False) 
    deadline = models.DateTimeField(null=True)

class Categorize(models.Model):
    tag  = models.ForeignKey(Tag, on_delete=models.CASECADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASECADE)

class Done(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASECADE)
    done_date = models.DateField(auto_now_add = True)