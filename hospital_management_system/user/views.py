from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserRegisterForm
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=['post'])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        login(request, user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home_page')
    else:
        form = UserRegisterForm()

    return render(request, 'user/register.html', {'form': form})


def home_page(request):
    return render(request, "index.html")
