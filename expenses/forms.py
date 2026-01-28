from django import forms
from .models import Transaction
from django.utils import timezone

class AddTransactionForm(forms.ModelForm):
    transaction_date = forms.DateField(required=False)
    class Meta:
        model = Transaction
        fields = [
            'wallet',
            'category',
            'amount',
            'transaction_type',
            'title_field',
            'description',
            'transaction_date',
        ]

    def clean(self):
        cleaned_data = super().clean()
        if not cleaned_data.get("transaction_date"):
            cleaned_data["transaction_date"] = timezone.now().date()
        return cleaned_data