from django.contrib import admin
from django.urls import path
from doctorsApp import views

urlpatterns = [
    path('doctors/', views.DoctorsListPage.as_view(), name='doctors_list'),
    path('doctors/<int:doctor_id>/', views.DoctorDetailPage.as_view(), name='doctor_detail'),
]
