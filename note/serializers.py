from rest_framework import serializers
from .models import Note



class NoteSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Note
        fields = '__all__'
        read_only_fields = ['created_datetime']

