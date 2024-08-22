from django.urls import path
from .views import TaskListCreate, TaskDelete

urlpatterns = [
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDelete.as_view(), name='task-delete'),
]
