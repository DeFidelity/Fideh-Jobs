from django.db import models
from django.conf import settings

class Job(models.Model):
    title = models.CharField(max_length=223)
    description = models.TextField()
    detail = models.TextField(blank=True, null=True)
    duration = models.CharField(max_length=200,blank=True, null=True)
    payment_range = models.CharField(max_length=200,blank=True, null=True)
    remote = models.BooleanField(default=False,blank=True, null=True)
    experience = models.CharField(max_length=200,blank=True, null=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='jobs',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    change_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
class Application(models.Model):
    job = models.ForeignKey(Job,related_name='application', on_delete=models.CASCADE)
    proposal = models.TextField()
    experience = models.TextField(blank=True, null=True)
    payment = models.CharField(max_length=222,blank=True, null=True)
    delivery = models.CharField(max_length=222,blank=True, null=True)
    
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='application',on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    