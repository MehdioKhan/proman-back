from rest_framework import serializers
from .models import Project,Membership,TaskStatus
from account.serializers import UserSerializer,RoleSerializer


class CreateMembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ('id','user','project','role','is_admin')


class RetrieveMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = RoleSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ('id','user','project','role','is_admin')


class ListMembershipSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Membership
        fields = ('id','user','role','is_admin')


class TaskStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskStatus
        fields = ('id','name','color','project')


class ProjectSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Project
        fields = ('id','name','description','owner','members','tags')


class ListProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','name','description','owner')


class RetrieveProjectSerializer(serializers.ModelSerializer):
    permissions = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id','name','description','owner','members','permissions','tags')

    def get_permissions(self,obj):
        user = self.context.get('request').user
        membership = obj.memberships.filter(user=user).first()
        permissions = membership.role.permissions
        return permissions
