from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("carreras/", views.carreras, name="carreras"),
    path("docentes/", views.docentes, name="docentes"),
]