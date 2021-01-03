from django.db import models
from se_core.models.mixins import TimeStampedMixIn


class HashTag(TimeStampedMixIn):
    name = models.CharField(max_length=32)

