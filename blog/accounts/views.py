from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not email or not password1 or not password2:
            return render(request, "signupPage.html", {"error": "All fields are required"})

        if password1 != password2:
            return render(request, "signupPage.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "signupPage.html", {"error": "Username already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("login")

    return render(request, "signupPage.html")


def loginPage(request):
    # Always allow the login page to render, even for authenticated users.
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("record")

        return render(request, "loginPage.html", {
            "error": "Invalid username or password"
        })

    return render(request, "loginPage.html")

def logoutPage(request):
    logout(request)
    return render(request, "logoutPage.html")
