from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from .tagging.models import TagMixin


class Project(TagMixin):
    name = models.CharField(max_length=250,null=False,
                            blank=False,
                            verbose_name=_('name'))
    slug = models.SlugField(max_length=300,null=False,blank=True,
                            verbose_name=_('slug'))
    description = models.CharField(max_length=250, blank=True)
    owner = models.ForeignKey(to=get_user_model(),
                              related_name='owned_projects',
                              on_delete=models.CASCADE,
                              verbose_name=_('owner'))
    members = models.ManyToManyField(to=get_user_model(),
                                     through='Membership',
                                     through_fields=('project', 'user'),
                                     related_name='projects',
                                     verbose_name=_('members'))

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'
        ordering = ('name','id')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


class Membership(models.Model):
    user = models.ForeignKey(to=get_user_model(),
                             null=True,blank=True,
                             related_name='memberships',
                             on_delete=models.CASCADE,
                             verbose_name=_('user'))
    project = models.ForeignKey(to='Project',
                                null=False,blank=False,
                                related_name='memberships',
                                on_delete=models.CASCADE,
                                verbose_name=_('project'))
    role = models.ForeignKey(to='account.Role',
                             related_name='memberships',
                             on_delete=models.CASCADE,
                             verbose_name=_('role'))
    is_admin = models.BooleanField(default=False, null=False,
                                   blank=False,
                                   verbose_name=_('is admin'))

    class Meta:
        verbose_name = 'membership'
        verbose_name_plural = 'memberships'
        unique_together = ('user', 'project')
        ordering = ('project', 'user__email')


class TaskStatus(models.Model):
    name = models.CharField(max_length=55,null=False,blank=False,
                            verbose_name=_('name'))
    color = models.CharField(max_length=20,null=False,blank=False,
                             verbose_name=_('color'))
    project = models.ForeignKey(to='Project',on_delete=models.CASCADE,
                                related_name='task_statuses',
                                verbose_name=_('project'))

    class Meta:
        verbose_name = 'task status'
        verbose_name_plural = 'task statuses'
        ordering = ('project','name')
        unique_together = (('project','name'),)

    def __str__(self):
        return self.name
