from django.shortcuts import render
from rest_framework import generics
from .models import AppUser
from .serializers import AppUserSerializer
from rest_framework.decorators import api_view
from .models import AppUser
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view

class AppUserListCreateAPIView(generics.ListCreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


class AppUserDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AppUser.objects.all()
    serializer_class = AppUserSerializer


@api_view(['POST'])
def sign_up(request):
    if request.method == 'POST':
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not (username and email and password):
            return Response({"error": "Please provide username, email, and password"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = AppUser.objects.create_user(username=username, email=email, password=password)
            return Response({"success": "User created successfully"}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # User credentials are correct, generate token
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'username': user.username,
            'email': user.email,
            'token': token.key
        })
    else:
        # User credentials are incorrect
        return Response({'error': 'Invalid username or password'}, status=400)



    
    
