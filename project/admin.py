from django.contrib import admin
from .models import Project,Membership,TaskStatus

admin.site.register([Project,Membership,TaskStatus])