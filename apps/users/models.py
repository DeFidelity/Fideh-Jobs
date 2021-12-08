from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from .managers import CustomUserManager
from apps.job.models import Application
from django.dispatch import receiver
from django.db.models.signals import post_save

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser,related_name='profile',on_delete=models.CASCADE)
    is_employer = models.BooleanField(default=False)
    username = models.CharField(max_length=222,blank=True,null=True)
    field = models.CharField(max_length=30,blank=True,null=True)
    about = models.CharField(max_length=500,blank=True,null=True)
    country = models.CharField(max_length=120,blank=True,null=True)
    qualification = models.CharField(max_length=150,blank=True,null=True)
    age = models.PositiveIntegerField(blank=True,null=True)
    contact = models.CharField(max_length=222,blank=True, null=True)
    gender = models.CharField(max_length=30,blank=True,null=True)
    experience = models.CharField(max_length=222,blank=True, null=True)
    education = models.CharField(max_length=222,blank=True,null=True)
    status = models.BooleanField(default=True)
  
    def __str__(self):
        return self.username
    
class Conversation(models.Model):
    application = models.ForeignKey(Application,related_name="applicationconversation",on_delete=models.CASCADE)
    message = models.TextField()
    created_by = models.ForeignKey(CustomUser,related_name="applicationconversation",on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_on']
        
    def __str__(self):
        return str(self.application) + 'conversation'
    
    
    
@receiver(post_save, sender=CustomUser)
def update_user_profile(sender, instance, created, **kwargs):
    """
    Signals the Profile about User creation.
    """
    if created:
        UserProfile.objects.create(user=instance)
    instance.profile.save()
    
@receiver(post_save, sender=CustomUser)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()

