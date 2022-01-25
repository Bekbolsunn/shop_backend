from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


# from django.shortcuts import render
# from rest_framework.authtoken.admin import User
# from user.serializer import UserRegisterValidateSerializer

@api_view(['POST'])
def login(request):
    """Авторизация"""
    if request.method == 'POST':
        user = authenticate(**request.data)
        """Если он существует то отправляем Token"""
        if user:
            """Если зайдут с другого устр то этот удалиться только 1 может быть"""
            Token.objects.filter(user=user).delete()
            token = Token.objects.create(user=user)
            return Response(data={'token': token.key})
        return Response(data={'message': 'User not found!'},
                        status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        User.objects.create_user(username=username, password=password)
        return Response(data={'message': 'User created!'})
    return Response(data={'message': 'User already registered!'})


"""
Домашнее задание 5.
Написать регистрацию
Написать авторизацию
Extra Task: При регистрации отправить письмо для подтверждения на почту. 
При переходе из письма активировать пользователя.
"""
