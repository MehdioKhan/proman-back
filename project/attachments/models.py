from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Attachments(models.Model):
    owner = models.ForeignKey(to=get_user_model(),
                              null=True,blank=True,
                              related_name='attachments',
                              on_delete=models.CASCADE,
                              verbose_name=_("owner"))
    project = models.ForeignKey(to='project.Project',
                                null=False,blank=False,
                                related_name='attachments',
                                on_delete=models.CASCADE,
                                verbose_name=_('project'))
    name = models.CharField(max_length=500,blank=True,default="")
    file = models.FileField(null=True,blank=True,
                            upload_to='attachments',
                            verbose_name=_("file"))

    class Meta:
        verbose_name = 'attachment'
        verbose_name_plural = 'attachments'
        ordering = ('name',)
