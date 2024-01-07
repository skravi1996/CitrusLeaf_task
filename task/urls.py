from django.urls import path
from .views import register, login, create_task, task_list, edit_task, delete_task

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('create-task/', create_task, name='create-task'),
    path('task-list/', task_list, name='task-list'),
    path('edit-task/<int:pk>/', edit_task, name='edit-task'),
    path('delete-task/<int:pk>/', delete_task, name='delete-task'),
]
