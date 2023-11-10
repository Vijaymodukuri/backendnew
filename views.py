from django.shortcuts import render

# Create your views here.
# myapp/views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from .models import CustomUsers
from .serializers import pUserSerializer
from rest_framework.permissions import IsAuthenticated

class RegistrationView(APIView):
    def get(self, request, format=None):
        # Implement logic to retrieve user information here
        # For example, retrieve a list of users
        users = CustomUsers.objects.all()
        serializer = pUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
   

    def post(self, request, format=None):
        serializer = pUserSerializer(data=request.data,many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)  # Print validation errors
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        print(request.data)
        username = request.data.get('user')
        password = request.data.get('password')
        authenticated_user = authenticate(request, username=username, password=password)
        if authenticated_user:
            login(request, authenticated_user)
            serializer = pUserSerializer(authenticated_user)
            return Response(serializer.data)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_201_CREATED)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request.auth.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)