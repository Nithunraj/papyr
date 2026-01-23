from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.expense_by_category, name="expense_category"),
    path('filter_details/', views.filter_details_transactions, name="filter_details"),
]
