from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Attachment(models.Model):
    owner = models.ForeignKey(to=get_user_model(),
                              null=True,blank=True,
                              related_name='attachments',
                              on_delete=models.CASCADE,
                              verbose_name=_("owner"))
    name = models.CharField(max_length=500,blank=True,default="")
    file = models.FileField(null=True,blank=True,
                            upload_to='attachments',
                            verbose_name=_("file"))
    size = models.PositiveIntegerField(blank=True,null=False,
                                       verbose_name=_("size"))
    task = models.ForeignKey(to='task.Task',
                             blank=False,null=False,
                             verbose_name=_("task"),
                             on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'
        ordering = ('name',)

    def save(self,*args,**kwargs):
        self.size = self.file.size
        super(Attachment, self).save(*args,**kwargs)

    def __str__(self):
        return "Attachment: {}".format(self.id)

