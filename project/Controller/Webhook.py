import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from project.Models.Lead import Lead 

@csrf_exempt
def Webhook(request):
    if request.method != "POST":
        return JsonResponse({"error":"Method not allowed"}, status=405) #Method Not Allowed- Someone sends GET instead of POST
    
    try:
        data=json.loads(request.body)
        name=data.get("name")
        email=data.get("email")
        phone=data.get("phone")
        source=data.get("source")

        if not name or (not email and not phone):
            return JsonResponse({"error":"Missing Required fields"},status=400)  #Bad Request Invalid JSON /missing required data

        if email and Lead.objects.filter(email=email).exists():
            return JsonResponse({"message":"Lead with this email already exists"}, status=200)
        
        if phone and Lead.objects.filter(phone=phone).exists():
            return JsonResponse({"message":"Lead with this phone number already exists"},status=200)
        
        lead=Lead.objects.create(
            name=name,
            email=email,
            phone=phone,
            source=source,
        )
        return JsonResponse({"message": "Lead Created Successfully", "lead_id": lead.id}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({"error":"Invalid JSON"}, status=400)

# 500 Internal Server Error - Error in your Django code