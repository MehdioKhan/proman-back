from rest_framework import viewsets
from rest_framework.permissions import  IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from .serializers import  NoteSerializer
from .models import Note



class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
    permission_classes = (IsAuthenticated,)
    authentication_classes = (BasicAuthentication,TokenAuthentication,)