from django import forms
from .models import Job, Application

class JobCreateForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'description','detail','duration','payment_range','remote','experience']
        
class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['proposal','experience','payment','delivery']