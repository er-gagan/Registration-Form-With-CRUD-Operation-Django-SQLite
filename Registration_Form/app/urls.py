from app import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('Send_Student_Info',views.Send_Student_Info),
    path('show',views.show),
    path('edit',views.edit),
    path('Edit_Detail',views.Edit_Detail),
    
    path('delete',views.Delete),   
]