from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import UserModel
from .serializers import UserRegisterSerializer
from .serializers import UserLoginSerializer
from django.contrib.auth import login
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views import View
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token



@method_decorator(csrf_exempt, name='dispatch')
class UserRegisterView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User signed up successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer = self.serializer_class()
        return Response({'serializer': serializer.data})



@method_decorator(csrf_exempt, name='dispatch')
class HomePageView(APIView):
    def get(self, request):
        return Response({'message': 'Welcome to the home page!'})
    
    

class UserLoginView(APIView):
    serializer_class = UserLoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            password = serializer.validated_data.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({"message": "User signed in successfully."}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid credentials."}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request):
        serializer = self.serializer_class()
        return Response({'serializer': serializer.data})


class UserLogoutView(APIView):
    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
    
    
    

    
    

    
    
