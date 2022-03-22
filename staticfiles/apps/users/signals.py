from django.db.models.signals import post_save #Import a post_save signal when a user is created
from .models import CustomUser# Import the built-in User model, which is a sender
from django.dispatch import receiver # Import the receiver
from .models import UserProfile


@receiver(post_save, sender=CustomUser) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()