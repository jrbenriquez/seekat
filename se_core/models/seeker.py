from django.db import models

from se_core.models.mixins import TimeStampedMixIn

# Create your models here.


class Seeker(TimeStampedMixIn):
    user = models.OneToOneField('authentication.User', related_name='seeker', on_delete=models.CASCADE)
    last_login = models.DateTimeField(auto_now_add=True)



