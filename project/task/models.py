from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.contrib.contenttypes.fields import GenericRelation
from project.tagging.models import TagMixin
from project.due_date.models import DueDateMixin


class Task(TagMixin,DueDateMixin,models.Model):
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
    subject = models.TextField(blank=False,null=False,
                               verbose_name=_("subject"))
    description = models.TextField(blank=True,null=False,
                                   verbose_name=_("description"))
    assigned_to = models.ForeignKey(to=get_user_model(),
                                    null=True,blank=True,
                                    default=None,
                                    related_name='assigned_tasks',
                                    on_delete=models.CASCADE,
                                    verbose_name=_('assigned to'))
    attachments = GenericRelation('attachments.Attachment')

    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'
        ordering = ('project','status')


class Comment(models.Model):
    user = models.ForeignKey(to=get_user_model(),
                             blank=False,null=False,
                             related_name='comments',
                             on_delete=models.CASCADE,
                             verbose_name=_("user"))
    task = models.ForeignKey(to=Task,blank=False,null=False,
                             related_name='comments',
                             on_delete=models.CASCADE,
                             verbose_name=_("task"))
    text = models.TextField(blank=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
