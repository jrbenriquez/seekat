from django.db import models

from se_core.models.mixins import TimeStampedMixIn
from se_core.models.constants import NAME_MAX_LENGTH

# TODO Follower Relations https://stackoverflow.com/questions/58794639/how-to-make-follower-following-system-with-django-model


class Seeker(TimeStampedMixIn):
    user = models.OneToOneField('authentication.User', related_name='seeker', on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now_add=True)
    public_name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
    first_name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
    last_name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
    #photo = models.ImageField()

    @property
    def username(self):
        return self.user.username

    @property
    def email(self):
        return self.user.email
