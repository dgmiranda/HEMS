# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    moto = models.CharField(max_length= 100, default='life is good')
    device1 = models.CharField(max_length= 100, default='yo1')
    device2 = models.CharField(max_length= 100, default='yo2')
    device3 = models.CharField(max_length= 100, default='yo3')
    voltage1 = models.IntegerField(default=120)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
