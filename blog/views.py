from rest_framework import viewsets,response
from rest_framework.permissions import IsAuthenticated
from .serializers import BlogSerializer
from .models import  Blog



class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all()
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def list(self, request, *args, **kwargs):
        author = request.GET.get('author',None)
        if author:
            blogs = self.queryset.filter(author=author)
            serializer = self.get_serializer_class()(blogs,many=True)
            return response.Response(serializer.data)
        else:
            return super(BlogViewSet, self).list(self,request,args,kwargs)

