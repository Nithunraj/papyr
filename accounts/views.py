from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomUserCreationForm
from django.contrib import messages

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
        form = CustomUserCreationForm()

    return render(request, "accounts/register.html", {"form": form})