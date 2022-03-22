from django import forms
from .models import Contact

class UserForm(forms.Form):
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    
class LoginForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
    first_name = forms.CharField(required=False)
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name','email','message')