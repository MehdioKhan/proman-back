from rest_framework import viewsets
from .serializers import TaskStatusSerializer,\
    ProjectSerializer,MembershipSerializer
from .models import Project,TaskStatus,Membership


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class TaskStatusViewSet(viewsets.ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()


class MembershipViewSet(viewsets.ModelViewSet):
    serializer_class = MembershipSerializer
    queryset = Membership.objects.all()
