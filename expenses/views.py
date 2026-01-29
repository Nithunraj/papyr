from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from .models import Transaction
from .forms import AddTransactionForm as UpdateTransactionForm
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

def update_transactions(request):
    if request.method == "POST":
        instance = get_object_or_404(Transaction, id=request.POST.get("id"))
        form = UpdateTransactionForm(request.POST, instance=instance)

        if form.is_valid():
            form.save()
            messages.success(request,"Sucessfully updated")
            return redirect('dashboard')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, field + ' - ' + error)
    return redirect('dashboard')