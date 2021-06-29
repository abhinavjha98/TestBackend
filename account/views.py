from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from account.utils import validate_data,register_user,get_tokens_for_user
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
User = get_user_model()
# from core.models import User
token=""

class UserAuthView(viewsets.ViewSet):   

    def signup(self, request):
        try:
            data = request.data
            print(data)
            validate, message = validate_data(data)
            if validate:
                user = register_user(**data)
                token = get_tokens_for_user(user)
                return Response(
                    data={'status': True, 'message': 'Authentication successfull', 'token': token}, 
                    status=status.HTTP_200_OK)
            else:
                return Response(
                    data={'status': True, 'message': message}, 
                    status=status.HTTP_200_OK)
        except Exception as e:
            return Response(
                    data={'status': False, 'message': str(e)}, 
                    status=status.HTTP_400_BAD_REQUEST)
    
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is None:
            return Response(
                data={'status': False, 'message': 'Invalid Credential'}, 
                status=status.HTTP_400_BAD_REQUEST)
        else:
            token = get_tokens_for_user(user)
            return Response(
                data={'status': True, 'message': 'Authentication successfull', 'token': token}, 
                status=status.HTTP_200_OK)