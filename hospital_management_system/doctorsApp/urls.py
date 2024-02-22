from django.contrib import admin
from django.urls import path
from doctorsApp import views

urlpatterns = [
    path('doctors/', views.DoctorViewSet.as_view({'get': 'list', 'post': 'create'}), name='doctors_list'),
    path('doctors/<int:doctor_id>/', views.DoctorViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='doctor_detail'),
]
