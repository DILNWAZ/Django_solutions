import token
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from .emails import send_verification_email
from rest_framework import status
from rest_framework_simplejwt.tokens import UntypedToken, TokenError

# Create your views here.

class RegisterAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            print('data is :',data)
            # serializer = UserSerializer(data=data)
            if serializers.is_valid():
                user = serializers.save()
                print(user)
                print(user.email)
                send_verification_email(user.email)
                return Response({
                    'status': 200,
                    'message': 'Reggistration successfully',
                    'data': serializers.data,
                }, status=status.HTTP_201_CREATED)
            return Response ({
                'status': 400,
                    'message': 'invalid data. please try again',
                    'data': serializers.error,
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message' : 'internal server Error.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VerifyAccount(APIView):
    def get(self,request):
        try:
            UntypedToken(token)
            return Response({
                'status': 200,
                'message' : 'token is valid.',
            }, status=status.HTTP_200_OK)
        except TokenError:
            return Response({
                'status': 400,
                'message' : 'invalid token.',
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message' : 'internal server Error.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)