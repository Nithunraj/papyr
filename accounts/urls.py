from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.login_view, name='login'),
    path("logout/", views.logout_view, name='logout'),
    path("register_user/", views.register_user, name='register_user'),
    path("view_my_profile/", views.view_my_profile, name='profile'),
    path("update_password/", views.updatePassword, name='update_password'),
    path("home/", include('dashboard.urls')),
    path("api/expenses/", include('expenses.urls')),
]
