from django.contrib import admin

from .models import Contact 

class ContactDisplay(admin.ModelAdmin):
    list_display = ['name','email','message','date']
    
    
admin.site.register(Contact,ContactDisplay)