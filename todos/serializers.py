from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        models = Todo
        fields = ('id','owner','content', 'tags', 'success','deadline')

class DoneTodoSerailizer(serializers.ModelSerializer):
    class Meta:
        models = DoneTodo
        fields = ('id', 'todo', 'done_date')