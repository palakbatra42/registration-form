from django.shortcuts import render,redirect
from rest_framework.decorators import api_view
from project.Models.Lead import Lead
from project.Models.LeadStatusHistory import LeadStatusHistory
from ..Serializers import LeadSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework.views import exception_handler
from django.urls import reverse
from django.contrib.auth.decorators import login_required

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def Lead_list(request):
    leads = Lead.objects.all()
    serializer = LeadSerializer(leads, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def Add_list(request):
    print(request.data)
    
    serializer = LeadSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def Update_list(request, pk): 
    #PUT
    try:
        lead = Lead.objects.get(id=pk)
    except Lead.DoesNotExist:
        return Response({"error": "Lead not found"},status=status.HTTP_404_NOT_FOUND)

    #GET
    if request.method == 'GET':
        Serializer = LeadSerializer(lead)
        return Response(Serializer.data)
    
    #PATCH
    if request.method == 'PATCH':
        Serializer = LeadSerializer(lead, data=request.data, partial=True)
    else:
        Serializer = LeadSerializer(lead, data=request.data)

    if Serializer.is_valid():
        Serializer.save()
        return Response(Serializer.data)
    return Response(Serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#DELETE
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])  
def Delete_list(request, pk):
    try:
        lead = Lead.objects.get(id=pk)
        lead.delete()

        return Response(
            {"message": "Lead deleted successfully"},
            status=status.HTTP_200_OK
        )

    except Lead.DoesNotExist:
        return Response(
            {"message": "Lead data already deleted"},
            status=status.HTTP_404_NOT_FOUND
        )

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response:
        response.data = {
            "detail": response.data.get("detail", "Error occurred"),
            "code": getattr(exc, "default_code", "error"),
            "messages": [
                {
                    
                    "type": exc.__class__.__name__
                }
            ]
        }
    return response


# adjust import path to match where your Lead model actually lives

@login_required(login_url='/login/')
def Pick_action(request):
    if request.method == "POST":
        pk = request.POST.get("pk")
        action = request.POST.get("action")

        if pk and action in ("Update", "Delete"):
            url_name = f"Api:{action}"
            return redirect(reverse(url_name, args=[pk]))

    leads = Lead.objects.all().order_by('id')
    return render(request, "Dashboard/pick_action.html", {"leads": leads})

#GIT COMMANDS USED TO UPLOAD PROJECT TO GITHUB

# git status
# git add .
# git commit -m "Updated project files"
# git push origin main