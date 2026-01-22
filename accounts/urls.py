from django.urls import path, include
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path("", views.login_view, name='login'),
    path("logout/", LogoutView.as_view(), name='logout'),
    path("register_user/", views.register_user, name='register_user'),
    path("view_my_profile/", views.view_my_profile, name='profile'),
    # path("update_my_profile/", views.update_my_profile, name='update_profile'),
    path("home/", include('dashboard.urls')),
    path("api/expenses/", include('expenses.urls')),
]
