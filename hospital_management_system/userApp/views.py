from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import UserModel
from .serializers import UserSerializer
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView


class UserRegisterView(APIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = self.serializer_class()
        return Response({'serializer': serializer.data})


class HomePageView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the home page!'})
