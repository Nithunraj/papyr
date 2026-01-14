from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.login_view, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register_user/", views.register_user, name='register_user'),
    path("home/", include('dashboard.urls')),
    path("api/expenses/", include('expenses.urls')),
]
