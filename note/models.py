from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Note(models.Model):
    author = models.ForeignKey(to=get_user_model(),
                               null=False, blank=False,
                               related_name='notes',
                               verbose_name=_('author'),
                               on_delete=models.CASCADE)

    title = models.CharField(verbose_name=_('Note Title'),max_length=100)

    created_datetime = models.DateTimeField(auto_now_add=True,
                                            verbose_name=_('created date'))

    description = models.TextField(verbose_name=_('Note Content'))

    class Meta:
        verbose_name = _("Note")
        verbose_name_plural = _("Notes")

    def __str__(self):
        return self.title
