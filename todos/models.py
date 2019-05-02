from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    tag = models.CharField(max_length=200, null=True)
    success = models.BooleanField(default=False) 
    deadline = models.DateTimeField(null=True)

class DoneTodo(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    done_date = models.DateField(auto_now_add = True)