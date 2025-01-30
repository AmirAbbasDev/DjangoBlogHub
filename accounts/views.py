from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


def register_view(request):
    if request.user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


# Logout
@login_required
def logout_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    if request.method == "POST":
        logout(request)
        return redirect("login")
    return redirect("index")


# Create your views here.
