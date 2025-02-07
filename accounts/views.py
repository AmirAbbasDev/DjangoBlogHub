from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.models import User


def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# Logout
@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect(reverse("login"))

    if request.method == "POST":
        logout(request)
        return redirect(reverse("login"))
    return redirect(reverse("index"))


# Create your views here.
