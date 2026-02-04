from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.expense_by_category, name="expense_category"),
    path('update_transactions/', views.update_transactions, name="update_transactions"),
]
