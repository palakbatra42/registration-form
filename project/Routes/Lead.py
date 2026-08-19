from django.urls import path
from project.Controller import Lead


urlpatterns = [
    path('add/', Lead.Add_lead, name='Add_lead'),
    path("update/<int:id>/", Lead.Update_lead, name="Update_lead"),
    path("delete/<int:id>/", Lead.Delete_lead, name="Delete_lead"),
    # path("update_status/<int:id>/",views.update_status,name="update_status"),
    

    path('home/', Lead.Home, name='Home'),
    path('record/', Lead.Record, name='Record'),
    path('export/csv/', Lead.Export_csv, name='Export_csv'),
    path('export/excel/', Lead.Export_excel, name='Export_excel'),
    path('update-status/<int:id>/', Lead.Update_status, name='Update_status'),
    path('detail/<int:id>/', Lead.Lead_detail, name='Lead_detail'),
    path('import/csv/',Lead.Import_csv, name='Import_csv'),
    path('document/',Lead.Api_document,name="Document"),
    path('detail/',Lead.Detail,name="Detail"),

    
]