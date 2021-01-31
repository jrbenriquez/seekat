from rest_framework.serializers import ModelSerializer

from se_api.v1.serializers.core import SESerializer
from se_core.models.seekat import Seekat
from se_core.models.address import SeekatAddress

class SeekatAddressSerializer(SESerializer):

    class Meta:
        model = SeekatAddress
        fields = [
            'id',
            'line1',
            'line2',
            'city',
            'state',
            'country',
            'name',
        ]

class SeekatSerializer(SESerializer):
    address = SeekatAddressSerializer(nested_dynamic_param='address')

    class Meta:
        model = Seekat
        nested_dynamic_fields = ['address']
        fields = [
            'id',
            'name',
            'description',
            'parent',
            'address',
        ]
