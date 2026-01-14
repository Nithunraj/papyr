from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Identity
    email = models.EmailField(unique=True)

    # Preferences
    currency = models.CharField(max_length=5, default='INR')
    timezone = models.CharField(max_length=50, default='Asia/Kolkata')
    language = models.CharField(max_length=10, default='en')

    # Security
    is_email_verified = models.BooleanField(default=False)
    two_factor_enabled = models.BooleanField(default=False)
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)

    # Account lifecycle
    account_status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('blocked', 'Blocked'),
            ('deleted', 'Deleted')
        ],
        default='active'
    )

    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    full_name = models.CharField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_completed = models.BooleanField(default=False)