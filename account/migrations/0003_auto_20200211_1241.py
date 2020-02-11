# Generated by Django 3.0 on 2020-02-11 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_auto_20200211_1238'),
        ('account', '0002_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='role',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roles', to='project.Project', verbose_name='Project'),
        ),
    ]
