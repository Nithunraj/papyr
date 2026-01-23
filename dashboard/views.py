from django.shortcuts import render,redirect
# from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from expenses.models import Transaction, Category, Wallet
from expenses.forms import AddTransactionForm

# Create your views here.
def dashboard(request):
    transactions = (
        Transaction.objects
        .filter(user=request.user)
        .select_related("wallet", "category")
        .order_by("-transaction_date")
    )

    wallets = Wallet.objects.filter(user=request.user, is_active=True)
    categories = Category.objects.filter(user=request.user)

    income_transactions = transactions.filter(
        transaction_type="income"
    )
    
    income = income_transactions.aggregate(total=Sum("amount"))["total"] or 0

    expense_transactions = transactions.filter(
        transaction_type="expense"
    )
    
    expense = expense_transactions.aggregate(total=Sum("amount"))["total"] or 0

    context = {
        "transactions": transactions,
        "wallets": wallets,
        "categories": categories,
        "income_total": income,
        "expense_total": expense,
        "balance": income - expense,
        "income_transactions": income_transactions,
        "expense_transactions":expense_transactions,
    }

    return render(request, "dashboard/dashboard.html", context)

def add_transactions(request):
    if request.method == "POST":
        form = AddTransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    return dashboard(request)