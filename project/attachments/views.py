from rest_framework import viewsets,permissions
from .models import Attachment
from .serializers import AttachmentsSerializer
from rest_framework.response import Response


class AttachmentsViewSet(viewsets.ModelViewSet):
    serializer_class = AttachmentsSerializer
    queryset = Attachment.objects.all()
    permission_classes = [permissions.IsAuthenticated,]

    def list(self, request, *args, **kwargs):
        task = request.GET.get('task',None)
        if not task:
            return Response({'error':'task id not provided.'},400)
        else:
            query = self.get_queryset().filter(task=task)
            serializer = self.get_serializer_class()(query)
            return Response(serializer.data)

