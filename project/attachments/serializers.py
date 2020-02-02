from rest_framework import serializers
from .models import Attachment


class AttachmentsSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()

    class Meta:
        model = Attachment
        fields = ('id','owner','project','name','file','size',
                  'url','object_id')

    def get_url(self,obj):
        return obj.file.url
