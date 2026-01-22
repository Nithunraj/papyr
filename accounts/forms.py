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

class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="Current Password"
    )

    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
        label="New Password"
    )