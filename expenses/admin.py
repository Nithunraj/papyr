from django.contrib import admin
from .models import Wallet, Category, Transaction

# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "balance", "currency", "is_active")
    list_filter = ("currency", "is_active")
    search_fields = ("name", "user__email")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "name", "type")
    list_filter = ("type",)
    search_fields = ("name", "user__email")

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "wallet",
        "category",
        "transaction_type",
        "amount",
        "transaction_date",
    )
    list_filter = ("transaction_type", "transaction_date")
    search_fields = ("description", "user__email")
    date_hierarchy = "transaction_date"
