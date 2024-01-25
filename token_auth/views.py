from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .token_serializer import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
def login(request):
    user = get_object_or_404(get_user_model(), email=request.data['email'])
    if not user.check_password(request.data['password']):
        return Response({'error': 'Wrong password'}, status=status.HTTP_400_BAD_REQUEST)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def signup(request):
    tokensrz = UserSerializer(data=request.data)
    if tokensrz.is_valid():
        tokensrz.save()
        user = get_user_model().objects.get(email=tokensrz.data['email'])
        user.set_password(tokensrz.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response({'token': token.key, 'user': tokensrz.data}, status=status.HTTP_201_CREATED)
    return Response(tokensrz.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def test_token(request):
    return Response(f'Passed for {request.user}')

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def reset_token(request):
    request.user.auth_token.delete()
    user = get_object_or_404(get_user_model(), email=request.user.email)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_token(request):
    request.user.auth_token.delete()
    return Response(f'Deleted for {request.user}', status=status.HTTP_200_OK)