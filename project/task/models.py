from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    owner = models.ForeignKey(to=get_user_model(),
                              null=True,blank=True,
                              default=None,
                              related_name='tasks',
                              on_delete=models.CASCADE,
                              verbose_name=_('owner'))
    project = models.ForeignKey(to='project.Project',
                                null=False,blank=False,
                                related_name='tasks',
                                on_delete=models.CASCADE,
                                verbose_name=_('project'))
    status = models.ForeignKey(to='project.TaskStatus',
                               null=True,blank=True,
                               on_delete=models.CASCADE,
                               related_name='tasks',
                               verbose_name=_('status'))

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ('project','status')
