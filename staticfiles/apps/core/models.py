from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100,blank=True)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.email)