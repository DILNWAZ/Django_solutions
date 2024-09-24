from django.shortcuts import render
from .models import Student
from .serializer import Student_serializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class studentModelViewSet(viewsets.ModelViewSet):
    query = Student.objects.all()
    serializer_class = Student_serializer
    authentication_classes = [BasicAuthentication]
    # Permission_classes = [IsAutenticated]
    Permission_classes = [IsAdminUser]





