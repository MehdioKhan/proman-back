from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _



class note(models.Model):
    user = models.ForeignKey(to=get_user_model(),
                             on_delete=models.CASCADE,
                             null=False,blank=False,
                             related_name='notes',
                             verbose_name=_('user'))

    created = models.DateTimeField(auto_now_add=True,
                                   null=False, blank=False,
                                   verbose_name=_('created date'))

    meme  = models.TextField(verbose_name=_('Note Content'))

