from rest_framework import serializers
from .models import Students

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    rol = serializers.IntegerField()
    city = serializers.CharField(max_length=255)


def create(self, validate_data):
    return Students.object.create(**validate_data)