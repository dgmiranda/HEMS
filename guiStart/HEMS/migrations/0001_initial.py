# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-11 18:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moto', models.CharField(default='life is good', max_length=100)),
                ('device1', models.CharField(default='yo1', max_length=100)),
                ('device2', models.CharField(default='yo2', max_length=100)),
                ('device3', models.CharField(default='yo3', max_length=100)),
                ('voltage1', models.IntegerField(default=120)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
