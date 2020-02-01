from django.db import models
from django.utils.translation import gettext_lazy as _


class DueDateMixin(models.Model):
    due_date = models.DateField(null=True,blank=True,default=None,
                                verbose_name=_("due date"))
    due_description = models.TextField(blank=True,null=True,
                                       default='',
                                       verbose_name=_("due description"))

    class Meta:
        abstract = True
