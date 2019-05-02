from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')

        def create(self, validated_data):
            user = User.objects.create_user(validated_data['username'], None, validated_data['password'])
            return user

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','owner','content', 'tag', 'success','deadline')

class DoneTodoSerailizer(serializers.ModelSerializer):
    class Meta:
        models = DoneTodo
        fields = ('id', 'todo', 'done_date')