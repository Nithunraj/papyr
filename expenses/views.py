from django.shortcuts import render
from django.http import JsonResponse
from .models import Transaction
from dashboard import views as dashboard_view
from django.db.models import Sum

# Create your views here.
def expense_by_category(request):
    user = request.user

    qs = (
        Transaction.objects
        .filter(user=user, transaction_type="expense")
        .values("category__name")
        .annotate(total=Sum("amount"))
    )

    data = {
        item["category__name"] or "Uncategorized": float(item["total"])
        for item in qs
    }

    print(data)

    return JsonResponse(data)

def filter_details_transactions(request):
    

    data = {}

    return JsonResponse(data)