from django.db import models
from django.db.models.fields import related
from apps.users.models import CustomUser 


class Notification(models.Model):
    MESSAGE = 'message'
    APPLICATION = 'application'
    
    CHOICES = {
        (MESSAGE, 'Message'),
        (APPLICATION, 'Application')
    }
    
    to_user = models.ForeignKey(CustomUser,related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=25,choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_pk = models.IntegerField(null=True,blank=True)
    created_by = models.ForeignKey(CustomUser,related_name="notificationby",on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created_at',)