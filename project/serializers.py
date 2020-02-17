from rest_framework import serializers
from .models import Project,Membership,TaskStatus
from account.serializers import UserSerializer,RoleSerializer
from account.models import Role


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

    def create(self, validated_data):
        permissions = ['change_project','delete_project','add_member',
                       'remove_member']
        project = Project.objects.create(**validated_data)
        role = Role.objects.create(name='admin',project=project)
        role.permissions = permissions
        role.save()
        mebership = Membership.objects.create(user=project.owner,
                                              project=project,
                                              role=role,
                                              is_admin=True)
        return project


class ListProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ('id','name','description','owner','tags')


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
