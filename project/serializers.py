from rest_framework import serializers
from .models import Project,Membership,TaskStatus
from account.serializers import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ('id','name','description','owner','members','tags')


class CreateMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ('id','user','project','role','is_admin')


class RetrieveMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ('id','user','project','role','is_admin')


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('id','name','color','project')

