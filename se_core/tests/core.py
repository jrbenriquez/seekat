from django.test import TestCase

from se_core.models import Seek
from se_core.models import Seeker
from se_core.models import Seekat

from se_core.tests.factory import SeekFactory


class CoreTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.seek = SeekFactory()

    def test_create_seeker(self):
        seekers = Seeker.objects.all()
        self.assertIsNotNone(seekers)

    def test_create_seekat(self):
        seekats = Seekat.objects.all()
        self.assertIsNotNone(seekats)

    def test_create_seek(self):
        seeks = Seek.objects.all()
        self.assertIsNotNone(seeks)
