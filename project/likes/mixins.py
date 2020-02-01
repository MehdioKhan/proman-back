from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.contrib.contenttypes.models import ContentType
from .models import Like


class LikeMixin(object):

    @api_view('POST')
    def like(self,request,pk=None):
        obj = self.get_object()
        obj_type = ContentType.objects.get_for_model(obj)
        like,created = Like.objects.get_or_create(content_type=obj_type,
                                                  object_id=obj.id,
                                                  user=request.user)
        return Response("Success",status=HTTP_200_OK)

    @api_view('POST')
    def unlike(self,request,pk=None):
        obj = self.get_object()
        obj_type = ContentType.objects.get_for_model(obj)
        objects = Like.objects.filter(content_type=obj_type,
                                      object_id=obj.id,
                                      user=request.user)
        if objects.exists():
            like = objects.first()
            like.delete()

        return Response("Success",status=HTTP_200_OK)
