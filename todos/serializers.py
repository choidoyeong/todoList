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

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', )

class TodoSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many = True)
    class Meta:
        models = Todo
        fields = ('id','owner','content', 'tags', 'success','deadline')

    def create(self, validated_data):
        tag_datas = validated_data.pop('tags')
        todo = Todo.objects.create(**validated_data)
        for tag_data in tag_datas:
            tag = Tag.objects.get_or_create(**tag_data)
            todo.tags.add(tag)
        return todo

class DoneTodoSerailizer(serializers.ModelSerializer):
    class Meta:
        models = DoneTodo
        fields = ('id', 'todo', 'done_date')