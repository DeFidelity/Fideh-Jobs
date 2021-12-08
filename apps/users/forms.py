from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, UserProfile


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)
        
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ['username','field','about','age','qualification','country','contact','gender','experience','education','status']