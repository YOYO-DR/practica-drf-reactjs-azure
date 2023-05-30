from rest_framework import viewsets
from .serializer import TaskSerializer 
from .models import Task

#vista que recibe las peticiones
class TaskView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset=Task.objects.all()