from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.username}'s profile"


@receiver(post_save, sender=Profile)
def _post_save_receiver(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

    else:
        instance.profile.save()
