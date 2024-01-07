from django.shortcuts import render, redirect
from django.contrib.auth import login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.views import View


class UserRegisterView(View):
    template_name = 'user/register.html'
    serializer_class = UserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return redirect('home_page')
        return render(request, self.template_name, {'serializer': serializer})

    def get(self, request):
        serializer = self.serializer_class()
        return render(request, self.template_name, {'serializer': serializer})


class HomePageView(View):
    template_name = 'index.html'

    def get(self, request):
        return render(request, self.template_name)
