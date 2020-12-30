from django.db import models

class SocialMediaMixin(models.Model):

    class SocialMediaPlatforms(models.TextChoices):
        FACEBOOK = 'FB', 'Facebook'
        TWITTER = 'TW', 'Twitter'
        INSTAGRAM = 'IG', 'Instagram'
        YOUTUBE = 'YT', 'YouTube'
        TWITCH = 'TWCH', 'Twitch'
        DISCORD = 'DS', 'Discord'

    platform = models.CharField(max_length=4, choices=SocialMediaPlatforms.choices)
    link = models.URLField(max_length=255)


class SeekerSocialMediaLink(SocialMediaMixin):
    seeker = models.ForeignKey('se_core.Seeker', related_name="social_media_links", on_delete=models.CASCADE)


class SeekatSocialMediaLink(SocialMediaMixin):
    seekat = models.ForeignKey('se_core.Seekat', related_name="social_media_links", on_delete=models.CASCADE)
