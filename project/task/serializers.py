from rest_framework import serializers
from .models import Task,Comment


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('user','task','text')


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)

    class Meta:
        model = Task
        fields = ('subject','description','assigned_to','attachments',
                  'comments','status')


class TaskListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ('id','subject','status')
