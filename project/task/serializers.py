from rest_framework import serializers
from .models import Task,Comment
from project.due_date.serializers import DueDateSerializerMixin


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user','task','text')


class TaskSerializer(DueDateSerializerMixin,serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    owner = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Task
        fields = ('owner','project','subject','description','assigned_to',
                  'comments','status','due_date','due_description',
                  'due_status')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','subject','status')
