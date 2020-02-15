from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,\
    TokenAuthentication
from .serializers import TaskStatusSerializer,\
    ProjectSerializer,CreateMembershipSerializer,\
    RetrieveMembershipSerializer
from .models import Project,TaskStatus,Membership


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]


class TaskStatusViewSet(viewsets.ModelViewSet):
    serializer_class = TaskStatusSerializer
    queryset = TaskStatus.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = Membership.objects.all()
    permission_classes = [IsAuthenticated,]
    authentication_classes = [BasicAuthentication,TokenAuthentication]

    def get_serializer_class(self):
        if self.action in ['list','retrieve']:
            return RetrieveMembershipSerializer
        else:
            return CreateMembershipSerializer
