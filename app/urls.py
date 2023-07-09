from app import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('save-info', views.save_info),
    path('show', views.show),
    path('edit', views.edit),
    path('edit-info', views.edit_info),

    path('delete', views.Delete),
]
