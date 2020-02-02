from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer,TaskListSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated,]

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        else:
            return TaskSerializer

    def list(self, request, *args, **kwargs):
        tasks = self.queryset.filter(owner=request.user)
        serializer = self.get_serializer_class()(tasks,many=True)
        return response.Response(serializer.data)
