from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, UserProfile

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['full_name', 'phone_number']