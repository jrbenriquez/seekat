from django.db import models
from se_core.models.mixins import TimeStampedMixIn
from se_core.models.constants import NAME_MAX_LENGTH


class Seekat(TimeStampedMixIn):
    name = models.CharField(max_length=NAME_MAX_LENGTH)
    address = models.ForeignKey('se_core.SeekatAddress', related_name='seekats', on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class SeekatUser(TimeStampedMixIn):
    user = models.OneToOneField('authentication.User', related_name='seekat_user', on_delete=models.CASCADE)


class SeekatGroup(TimeStampedMixIn):
    """ SeekatGroups are a group of users that solely represent a Seekat"""
    members = models.ManyToManyField('se_core.SeekatUser', related_name='seekat_groups')

