from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),  
    path("SampleTable", views.SampleTable, name="SampleTable"), 
    path("StudentTable", views.StudentTable, name="StudentTable"), 
    path("StudentTable/<int:id>", views.StudentDetail, name="StudentDetail"), 
]
