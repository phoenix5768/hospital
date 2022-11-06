from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('adminpage', views.adminpage, name="adminpage"),
    path('patient', views.patient, name="patient"),
    path('doctor', views.doctor, name="doctor"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('showp/<patient_id>', views.showp, name="showp"),
]
