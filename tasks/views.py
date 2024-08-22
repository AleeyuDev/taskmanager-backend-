from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDelete(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
