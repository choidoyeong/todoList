from django.urls import include, path
from . import views

urlpatterns = [
    path('users/<int:user_id>/todos/', views.TodoList.as_view()),
    path('users/<int:user_id>/todos/<int:todo_id>/', views.TodoDetail.as_view()),
    path('login/', views.SignIn.as_view()),
    path('signup/', views.SignUP.as_view()),
]