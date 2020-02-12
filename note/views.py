from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,\
    TokenAuthentication
from .serializers import  NoteSerializer
from .models import Note


class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = [BasicAuthentication,
                              TokenAuthentication]

    def list(self, request, *args, **kwargs):
        notes = self.queryset.filter(author=request.user)
        serializer = self.get_serializer_class()(notes,many=True)
        return response.Response(serializer.data)

