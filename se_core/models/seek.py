from django.db import models
from se_core.models.mixins import TimeStampedMixIn


class Seek(TimeStampedMixIn):
    seeker = models.ForeignKey('se_core.Seeker', related_name='seeks', on_delete=models.CASCADE)
    category = models.ForeignKey('se_core.Category', related_name='seeks', on_delete=models.SET_NULL, null=True, blank=True)
    seekat = models.ForeignKey('se_core.Seekat', related_name='seeks', on_delete=models.CASCADE)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    hashtags = models.ManyToManyField('se_core.HashTag', related_name="seeks")

    @property
    def vote_count(self):
        return self.upvote_count - self.downvote_count

