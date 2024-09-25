from django.shortcuts import render
from .models import Student
from .serializer import Student_serializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions

class studentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Student_serializer
    authentication_classes = [SessionAuthentication]
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    permission_classes = [DjangoModelPermissions]
    





