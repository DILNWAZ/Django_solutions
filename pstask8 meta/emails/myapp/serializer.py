from rest_framework import serializers
from .models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', 'is_verified']

    def create(self, validated_date):
        user = User(**validated_date)
        user.set_password(validated_date['password'])
        user.save()
        return user