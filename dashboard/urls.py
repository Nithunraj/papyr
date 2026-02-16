from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('data_overview/', views.data_overview, name='data_overview'),
    path('add_transactions/', views.add_transactions, name='add_transactions'),
]
