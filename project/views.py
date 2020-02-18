from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from . import serializers
from .models import Project,TaskStatus,Membership
from permissions.permissions import ProjectAdminPermission,\
    ProjectMembershipPermission


class ProjectViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,ProjectAdminPermission]
    queryset = Project.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.RetrieveProjectSerializer
        elif self.action == 'list':
            return serializers.ListProjectSerializer
        else:
            return serializers.ProjectSerializer

    def get_queryset(self):
        if self.action == 'list':
            owned_projects = Project.objects.filter(owner=self.request.user)
            member_projects = Project.objects.filter(memberships__user=self.request.user)
            queryset = owned_projects.union(member_projects)
            return queryset
        else:
            return super(ProjectViewSet, self).get_queryset()


class TaskStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    permission_classes = [IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project',None)
        if not project:
            return response.Response({'error':'project not provided'},404)
        statuses = self.queryset.filter(project=project)
        serializer = self.get_serializer_class()(statuses,many=True)
        return response.Response(serializer.data)


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [IsAuthenticated,ProjectMembershipPermission]

    def list(self, request, *args, **kwargs):
        project = request.GET.get('project',None)
        if not project:
            return response.Response({'error':'project not provided'},404)
        memberships = self.queryset.filter(project=project)
        serializer = self.get_serializer_class()(memberships,many=True)
        return response.Response(serializer.data)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.RetrieveMembershipSerializer
        elif self.action == 'list':
            return serializers.ListMembershipSerializer
        else:
            return serializers.CreateMembershipSerializer
