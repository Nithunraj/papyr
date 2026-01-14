from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add_transactions/', views.add_transactions, name='add_transactions'),
]
