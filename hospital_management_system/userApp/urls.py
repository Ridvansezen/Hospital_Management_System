from django.contrib import admin
from django.urls import path
from userApp import views

urlpatterns = [
    path('register/', views.UserViewSet.as_view({'post': 'register'}), name='user_register'),
    path('login/', views.UserViewSet.as_view({'get': 'login', 'post': 'login'}), name='user_login'),
    path('logout/', views.UserViewSet.as_view({'post': 'logout'}), name='user_logout'),
]

