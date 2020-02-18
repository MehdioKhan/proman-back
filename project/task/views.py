from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer,TaskListSerializer,\
    CommentSerializer
from .models import Task,Comment
from permissions.permissions import TaskPermission,CommentPermission


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated,TaskPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return TaskListSerializer
        else:
            return TaskSerializer

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project',None)
        if not project:
            return response.Response({'error':'project not provided'},404)
        tasks = self.queryset.filter(project=project)
        serializer = self.get_serializer_class()(tasks,many=True)
        return response.Response(serializer.data)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permission_classes = [IsAuthenticated,CommentPermission]

    def list(self, request, *args, **kwargs):
        task = request.GET.get('task',None)
        if not task:
            return response.Response({'error':'task_id not provided'},404)
        comments = self.queryset.filter(user=request.user,task=task)
        serializer = self.get_serializer_class()(comments,many=True)
        return response.Response(serializer.data)

