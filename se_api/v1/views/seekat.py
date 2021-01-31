from rest_framework.viewsets import ModelViewSet

from se_api.v1.serializers.seekat import SeekatSerializer
from se_core.models.seekat import Seekat


class SeekatViewSet(ModelViewSet):
    queryset = Seekat.objects.all()
    serializer_class = SeekatSerializer




