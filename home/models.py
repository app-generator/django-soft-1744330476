# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Nc(models.Model):

    #__Nc_FIELDS__
    number = models.TextField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Nc_FIELDS__END

    class Meta:
        verbose_name        = _("Nc")
        verbose_name_plural = _("Nc")


class Task(models.Model):

    #__Task_FIELDS__
    nc = models.ForeignKey(NC, on_delete=models.CASCADE)
    taskdescription = models.CharField(max_length=255, null=True, blank=True)

    #__Task_FIELDS__END

    class Meta:
        verbose_name        = _("Task")
        verbose_name_plural = _("Task")



#__MODELS__END
