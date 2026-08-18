from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def SignupPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        if not username or not email or not password1 or not password2:
            return render(request, "Register/SignupPage.html", {"error": "All fields are required"})

        if password1 != password2:
            return render(request, "Register/SignupPage.html", {"error": "Passwords do not match"})

        if User.objects.filter(username=username).exists():
            return render(request, "Register/SignupPage.html", {"error": "Username already exists"})

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        return redirect("Register:Login")

    return render(request, "Register/SignupPage.html")


def LoginPage(request):

    if request.user.is_authenticated:
        return redirect("Lead:Record")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password
        )
        if user is not None:
            login(request, user)
            return redirect("Lead:Record")

        return render(request, "Register/LoginPage.html", {
            "error": "Invalid username or password"
        })

    return render(request, "Register/LoginPage.html")


def LogoutPage(request):
    logout(request)
    return redirect("Register:Login")




# search for login_required
#  Get-ChildItem -Recurse -File -Filter *.py | Select-String "login_required"


# 1. Get-ChildItem
# Lists files and folders in the current directory.
# It is similar to dir in Windows.

# 2. -Recurse
# Searches inside all subfolders, not just the current folder.

# 3. -File
# Only considers files, not directories.

# 4. -Filter *.py
# Only selects Python files.
# So it searches files such as:
# views.py
# models.py
# urls.py
# settings.py

# 5. Select-String "login_required"
# Searches the contents of those Python files for the exact text: login_required