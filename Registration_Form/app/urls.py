from app import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('Send_Student_Info',views.Send_Student_Info),
]