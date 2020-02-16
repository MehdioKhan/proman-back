from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Blog(models.Model):
    author = models.ForeignKey(to=get_user_model(),
                               null=False, blank=False,
                               related_name='blogs',
                               verbose_name=_('author'),
                               on_delete=models.CASCADE)

    title = models.CharField(verbose_name=_('Blog Title'),
                             max_length=100)

    created_datetime = models.DateTimeField(auto_now_add=True,
                                            verbose_name=_('Created time of Blog'),
                                            )

    content = models.TextField(verbose_name=_('Blog Content'))

    class Meta:
        verbose_name = _('Blog')
        verbose_name_plural = _('Blogs')

    def __str__(self):
        return self.title