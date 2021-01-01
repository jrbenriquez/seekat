from django.db import models
from se_core.models.mixins import AddressMixin
from se_core.models.constants import NAME_MAX_LENGTH


class SeekatAddress(AddressMixin):
    name = models.CharField(max_length=NAME_MAX_LENGTH, null=True, blank=True)
