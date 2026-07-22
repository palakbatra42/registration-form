from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from leads.models import Lead
from .forms import LeadForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# from django.contrib import messages
# from django.db.models import Q

# def signupPage(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")

#         if not username or not email or not password1 or not password2:
#             return render(request, "signupPage.html", {"error": "All fields are required"})

#         if password1 != password2:
#             return render(request, "signupPage.html", {"error": "Passwords do not match"})

#         if User.objects.filter(username=username).exists():
#             return render(request, "signupPage.html", {"error": "Username already exists"})

#         User.objects.create_user(
#             username=username,
#             email=email,
#             password=password1
#         )

#         return redirect("login")

#     return render(request, "signupPage.html")


def loginPage(request):
    # Always allow the login page to render, even for authenticated users.
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")

        return render(request, "loginPage.html", {
            "error": "Invalid username or password"
        })

    return render(request, "loginPage.html")

# @login_required(login_url="login")
# def dashboard(request):
#     return render(request, "dashboard.html")

# def home(request):
#     form = LeadForm()
#     context = {
#         'form': form,
#     }
#     return render(request, "home.html", context)



def home(request):
    if request.method == "POST":
        form = LeadForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("record")

    else:
        form = LeadForm()

    return render(request, "home.html", {"form": form})






# def add_lead(request):
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("record")
#     else:
#         form = LeadForm()

#     data = Lead.objects.all()
#     context = {
#         'form': form,
#         'data': data,
#     }
#     return render(request, "home.html", context)


# def delete_lead(request, id):
#     lead = get_object_or_404(Lead, id=id)

#     if request.method == "POST":
#         lead.delete()
#         return redirect("record")

#     return render(request, "record.html", {"lead": lead})


# def update_lead(request, id):
#     lead = get_object_or_404(Lead, id=id)

#     if request.method == "POST":
#         form = LeadForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("record")
#     else:
#         form = LeadForm(instance=lead)

#     return render(request, "update.html", {"form": form})


# def logoutPage(request):
#     logout(request)
#     return redirect("login")



# def add_lead(request):
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect("record")
#     else:
#         form = LeadForm()

#     data = Lead.objects.all()
#     context = {
#         'form': form,
#         'data': data,
#     }
#     return render(request, "home.html", context)



# def delete_lead(request, id):
#     lead = get_object_or_404(Lead, id=id)

#     if request.method == "POST":
#         lead.delete()
#         return redirect("record")

#     return render(request, "record.html", {"lead": lead}
def record(request):
    
    form= LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)

        form.save()
        form=LeadForm()
    data=Lead.objects.all()
        
    context={
        'form':form,
        'data': data,             
    }
    return render(request, "record.html",context)

# def testing(request):
#     search = request.GET.get('search', '')
#     print("Search term:", search)   # Debugging

#     data = Lead.objects.all()
#     if search:
#         data = data.filter(name__icontains=search)
#         print("Results count:", data.count())   # Debugging

#     return render(request, 'record.html', {
#         'data': data,
#         'search': search,
#     })

# def testing(request):
    
#     search = request.GET.get('search', '')
#     status = request.GET.get('status', '')

#     data = Lead.objects.all()

#     if search:
#         data = data.filter(Q(name__icontains=search) | Q(email__icontains=search))

#     if status:
#         data = data.filter(status=status)

#     return render(request, 'record.html', {
#         'data': data,
#         'search': search,
#         'status': status,
#         'status_choices': Lead.STATUS_CHOICES,  # see note below
#     })


# def testing(request):
#     q = request.GET.get('q', '')

#     data = Lead.objects.all()

#     if q:
#         data = data.filter(
#             Q(name__icontains=q),
#             Q(email__icontains=q),
#             Q(phone__icontains=q)
#         )

#     context = {
#         'data': data,
#         'search': q,
#     }

#     return render(request, 'record.html', context)



# def testing(request):
#     q = request.GET.get('q', '').strip()

#     data = Lead.objects.all()

#     if q:
#         # Split by comma or space
#         words = q.replace(',', ' ').split()

#         query = Q()

#         for word in words:
#             query |= Q(name__icontains=word)
#             query |= Q(email__icontains=word)
#             query |= Q(phone__icontains=word)

#         data = data.filter(query).distinct()

#     return render(request, "record.html", {
#         "data": data,
#         "search": q,
#     })



def testing(request):

    name = request.GET.get("name", "")
    phone = request.GET.get("phone", "")
    email = request.GET.get("email", "")

    data = Lead.objects.all()

    if name:
        data = data.filter(name__icontains=name)

    if phone:
        data = data.filter(phone__icontains=phone)

    if email:
        data = data.filter(email__icontains=email)


    names = Lead.objects.values_list("name", flat=True).distinct()
    phones = Lead.objects.values_list("phone", flat=True).distinct()
    emails = Lead.objects.values_list("email", flat=True).distinct()

    return render(request, "record.html", {
        "data": data,
        "name": name,
        "phone": phone,
        "email": email,
        "names": names,
        "phones": phones,
        "emails": emails,
    })