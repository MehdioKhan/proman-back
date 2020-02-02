from rest_framework import viewsets
from .models import Attachment
from .serializers import AttachmentsSerializer
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404


class AttachmentsViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentsSerializer
    queryset = Attachment.objects.all()

    content_type = None
