from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify
from permissions.choices import MEMBERS_PERMISSIONS


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    username = None
    USERNAME_FIELD = 'email'

    email = models.EmailField(unique=True)

    REQUIRED_FIELDS = []
    objects = UserManager()

    def __str__(self):
        return self.email


class Role(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False,
                            verbose_name=_("Name"))
    project = models.ForeignKey(to='project.Project',blank=False,
                                null=False,related_name='roles',
                                verbose_name=_('Project'),
                                on_delete=models.CASCADE)
    permissions = ArrayField(models.TextField(null=False,
                            blank=False, choices=MEMBERS_PERMISSIONS),
                            null=True, blank=True, default=list,
                             verbose_name=_("permissions"))

    class Meta:
        verbose_name = _("Role")
        verbose_name_plural = _("Roles")
        ordering = ("name",)
        unique_together = (("name", "project"),)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Role, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

