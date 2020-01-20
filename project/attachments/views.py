from rest_framework import viewsets
from .models import Attachments
from .serializers import AttachmentsSerializer


class AttachmentsViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentsSerializer
    queryset = Attachments.objects.all()
