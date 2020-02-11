# Generated by Django 3.0 on 2020-02-11 08:47

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is admin')),
            ],
            options={
                'verbose_name': 'membership',
                'verbose_name_plural': 'memberships',
                'ordering': ('project', 'user__email'),
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, default=list, null=True, size=None, verbose_name='tags')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=300, verbose_name='slug')),
                ('description', models.CharField(blank=True, max_length=250)),
                ('members', models.ManyToManyField(related_name='projects', through='project.Membership', to=settings.AUTH_USER_MODEL, verbose_name='members')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_projects', to=settings.AUTH_USER_MODEL, verbose_name='owner')),
            ],
            options={
                'verbose_name': 'project',
                'verbose_name_plural': 'projects',
                'ordering': ('name', 'id'),
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='membership',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='project.Project', verbose_name='project'),
        ),
        migrations.AddField(
            model_name='membership',
            name='role',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to='project.Role', verbose_name='role'),
        ),
        migrations.AddField(
            model_name='membership',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='memberships', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.CreateModel(
            name='TaskStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='name')),
                ('slug', models.SlugField(blank=True, max_length=75, verbose_name='slug')),
                ('color', models.CharField(max_length=20, verbose_name='color')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_statuses', to='project.Project', verbose_name='project')),
            ],
            options={
                'verbose_name': 'task status',
                'verbose_name_plural': 'task statuses',
                'ordering': ('project', 'name'),
                'unique_together': {('project', 'slug'), ('project', 'name')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='membership',
            unique_together={('user', 'project')},
        ),
    ]
