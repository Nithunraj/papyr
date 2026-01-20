from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from decimal import Decimal

from expenses.models import Wallet, Category, Transaction
from accounts.models import UserProfile

User = get_user_model()

# Create default wallets and categories when a new user is created
@receiver(post_save, sender=User)
def create_default_wallets_and_categories(sender, instance, created, **kwargs):
    if not created:
        return

    # Default wallets
    Wallet.objects.bulk_create([
        Wallet(user=instance, name="Cash"),
        Wallet(user=instance, name="Bank"),
        Wallet(user=instance, name="UPI"),
    ])

    # Default categories
    Category.objects.bulk_create([
        Category(user=instance, name="Salary", type="income"),
        Category(user=instance, name="Business", type="income"),
        Category(user=instance, name="Food", type="expense"),
        Category(user=instance, name="Travel", type="expense"),
        Category(user=instance, name="Bills", type="expense"),
    ])

    UserProfile.objects.create(user=instance)

# Update wallet balance when a transaction is created
@receiver(post_save, sender=Transaction)
def update_wallet_balance_on_create(sender, instance, created, **kwargs):
    if not created:
        return

    wallet = instance.wallet
    if instance.transaction_type == 'income':
        wallet.balance += instance.amount
    else:
        wallet.balance -= instance.amount
    wallet.save(update_fields=["balance"])

# Reverse wallet balance when a transaction is deleted
@receiver(post_delete, sender=Transaction)
def update_wallet_balance_on_delete(sender, instance, **kwargs):
    wallet = instance.wallet
    if instance.transaction_type == 'income':
        wallet.balance -= instance.amount
    else:
        wallet.balance += instance.amount
    wallet.save(update_fields=["balance"])