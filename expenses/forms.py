from django import forms
from .models import Transaction

class AddTransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'wallet',
            'category',
            'amount',
            'transaction_type',
            'description',
            'transaction_date',
        ]