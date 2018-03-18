from django.db import models
from django.conf import settings
from django.db.models import signals


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    following = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='followed_by')

    def __str__(self):
        return str(self.following.all().count())

def post_save_get_or_create_user_profile(sender, instance, created, *args, **kwargs):
    if created:
        new_profile = UserProfile.objects.get_or_create(user=instance)

signals.post_save.connect(post_save_get_or_create_user_profile, sender=settings.AUTH_USER_MODEL)