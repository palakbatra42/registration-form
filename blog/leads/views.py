from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from leads.models import Lead
from .forms import LeadForm

def add_lead(request):
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("record")
    else:
        form = LeadForm()

    data = Lead.objects.all()
    context = {
        'form': form,
        'data': data,
    }
    return render(request, "home.html", context)


def delete_lead(request, id):
    lead = get_object_or_404(Lead, id=id)

    if request.method == "POST":
        lead.delete()
        return redirect("record")

    return render(request, "record.html", {"lead": lead})




# def update_lead(request, id):
#     lead = get_object_or_404(Lead, id=id)

#     if request.method == "POST":
#         form = LeadForm(request.POST, instance=lead)
#         if form.is_valid():
#             form.save()
#             return redirect("leads:add_lead")
#     else:
#         form = LeadForm(instance=lead)

#     data = Lead.objects.all()

#     context = {
#         "form": form,
#         "data": data,
#     }

#     return render(request, "update.html", context)











def update_lead(request, id):
    lead = get_object_or_404(Lead, id=id)

    if request.method == "POST":
        form = LeadForm(request.POST, instance=lead)

        if form.is_valid():
            form.save()
            return redirect("record")   # or redirect("leads:add_lead")

    else:
        form = LeadForm(instance=lead)

    return render(request, "update.html", {
        "form": form,
        "lead": lead,
    })