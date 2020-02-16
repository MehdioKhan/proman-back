from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,\
    TokenAuthentication
from . import serializers
from .models import Project,TaskStatus,Membership


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.RetrieveProjectSerializer
        else:
            return serializers.ProjectSerializer


class TaskStatusViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

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
