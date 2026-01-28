from django.db import models
from accounts.models import User
from django.utils import timezone

# Create your models here.
class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # Cash, Bank, UPI
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    currency = models.CharField(max_length=5, default='INR')
    is_active = models.BooleanField(default=True)

class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    type = models.CharField(
        max_length=10,
        choices=[('income','Income'), ('expense','Expense')]
    )

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_type = models.CharField(
        max_length=10,
        choices=[('income','Income'), ('expense','Expense')]
    )

    title_field = models.CharField(
    max_length=255,
    default="Untitled",
    null=True,
    blank=True
    )

    description = models.TextField(blank=True)
    transaction_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    monthly_limit = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.DateField()

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField()
    created_at = models.DateTimeField(auto_now_add=True)