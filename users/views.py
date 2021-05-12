from django.shortcuts import render
from rest_framework import generics, permissions
from .models import CustomUser
from .serializers import CustomUserSerializer


# Create your views here.


class UserList(generics.ListCreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
