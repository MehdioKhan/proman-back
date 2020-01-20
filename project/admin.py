from django.contrib import admin
from .models import Project,Membership,TaskStatus,Role

admin.site.register([Project,Membership,TaskStatus,Role])