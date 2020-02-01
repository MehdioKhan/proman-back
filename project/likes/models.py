from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Like(models.Model):
    content_type = models.ForeignKey(to=ContentType,
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    user = models.ForeignKey(to=get_user_model(),
                             null=False,blank=False,
                             on_delete=models.CASCADE,
                             related_name='likes',
                             verbose_name=_("user"))
    created = models.DateTimeField(auto_now_add=True,
                                   null=False,blank=False,
                                   verbose_name=_("created date"))

    class Meta:
        verbose_name = _("Like")
        verbose_name_plural = _("Likes")
        unique_together = ('content_type','object_id','user')
