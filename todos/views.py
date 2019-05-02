from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
# Create your views here.

class SignUP(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SignIn(APIView):
    serializer_class = UserSerializer
    def post(self, request, format=None):
        pass

class TodoList(APIView):
    serializer_class = TodoSerializer

    def get(self, request, user_id,format=None):
        todos = Todo.objects.filter(owner_id = user_id, success = False)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, user_id, format=None):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoDetail(APIView):
    serializer_class = TodoSerializer

    def get_object(self, todo_id):
        try:
            return Todo.objects.get(pk=todo_id)
        except Todo.DoesNotExist:
            raise Http404

    def put(self, request, user_id, todo_id, format=None):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, user_id, todo_id, format=None):
        todo = self.get_object(todo_id)
        serializer = TodoSerializer(todo, data = request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)