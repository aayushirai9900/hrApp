from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path("", views.create_profile,name="create_profile"),
    path("display",views.display_data, name='display'),
    
]
 