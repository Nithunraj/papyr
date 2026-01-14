from django.urls import path
from . import views

urlpatterns = [
    path('category/', views.expense_by_category, name="expense_category"),
]
