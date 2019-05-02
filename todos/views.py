from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
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
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user = User.objects.get(username=username)
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token), 'id': user.id}, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CheckID(APIView):
    def get(self, request, username):
        try:
            User.objects.get(username=username)
            return Response(status = status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)


class TodoList(APIView):
    serializer_class = TodoSerializer
    permission_classes = (IsAuthenticated,)

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
    permission_classes = (IsAuthenticated,)

    def get_object(self, todo_id):
        try:
            return Todo.objects.get(pk=todo_id)
        except Todo.DoesNotExist:
            raise Http404
    
    def delete(self, request, user_id, todo_id,format=None):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
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

class DoneTodoList(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = DoneTodoSerializer

    def get(self, request, user_id,format=None):
        todos = DoneTodo.objects.filter(owner = user_id)
        serializer = DoneTodoSerializer(todos, many=True)
        return Response(serializer.data)
    
    def post(self, request, user_id, format=None):
        serializer = DoneTodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoneTodoDetail(APIView):
    permission_classes = (IsAuthenticated,)
    def get_object(self, todo_id):
        try:
            return DoneTodo.objects.get(pk=todo_id)
        except DoneTodo.DoesNotExist:
            raise Http404

    def delete(self, request, user_id, todo_id,format=None):
        todo = self.get_object(todo_id)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    