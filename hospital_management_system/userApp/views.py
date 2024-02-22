from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import action
from .models import UserModel
from .serializers import UserRegisterSerializer, UserLoginSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserRegisterSerializer  # Default serializer

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def register(self, request, *args, **kwargs):
        if request.method == 'GET':
            # Get request, display form
            return Response({"message": "Display registration form"})

        # Post request, handle registration
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User signed up successfully.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get', 'post'])
    def login(self, request):
        if request.method == 'GET':
            return Response({"message": "GET Request", 'fields': {'username': '', 'password': ''}})

        if request.method == 'POST':
            # POST isteği geldiğinde normal işleyiş devam eder
            serializer = UserLoginSerializer(data=request.data)
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
        
        
    @action(detail=False, methods=['post'])
    def logout(self, request):
        # No serializer needed for logout action
        logout(request)
        return Response({"message": "User logged out successfully."}, status=status.HTTP_200_OK)
    
    
    @action(detail=False, methods=["get"])
    def home_page(self, request):
        return Response({"message":"Welcome to the home page!"})
