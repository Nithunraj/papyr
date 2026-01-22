from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm, UserProfileForm, ChangePasswordForm
from django.contrib import messages
from .models import UserProfile

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user:
            login(request, user)
            return redirect("dashboard")

        return render(request, "accounts/login.html", {
            "error": "Invalid credentials"
        })

    return render(request, "accounts/login.html")

def register_user(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Signals will handle default wallets & categories
            messages.success(request, "Account created successfully. Please log in.")
            return redirect("login")  # your login page
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})

def view_my_profile(request):
    profile, created = UserProfile.objects.get_or_create(user=request.user)
    changePasswordForm = ChangePasswordForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()

    profile, created = UserProfile.objects.get_or_create(user=request.user)
    form = UserProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {
        "form": form,
        "profile": profile,
        "passwordForm":changePasswordForm,
    })

@require_http_methods(["POST"])
def updatePassword(request):
    form = ChangePasswordForm()
    print(form)
    return redirect("profile")