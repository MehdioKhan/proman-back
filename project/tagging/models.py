from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _


class TagMixin(models.Model):

    tags = ArrayField(models.CharField(max_length=50),
                      null=True,
                      blank=True,
                      verbose_name=_('tags'),
                      default=list)

    class Meta:
        abstract = True
