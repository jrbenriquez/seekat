from django.db import models
from django_countries.fields import CountryField


class TimeStampedMixIn(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class AddressMixin(models.Model):

    class Meat:
        abstract = True

    address1 = models.CharField("Address Line 1", max_length=1024)
    address2 = models.CharField("Address Line 2", max_length=1024)
    zip_code = models.CharField("Zip/Postal Code", max_length=12)
    city = models.CharField("City", max_length=1024)
    state = models.CharField("State/Province", max_length=1024)
    country = CountryField()
    lon = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)

