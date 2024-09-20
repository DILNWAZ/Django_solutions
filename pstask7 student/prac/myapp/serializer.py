from rest_framework import serializers
from .models import Student,Course,Enrollment

class CourseSerializer(serializers.Serializer):
    course_id = serializers.CharField(max_length=10)
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=255)
    instructor = serializers.CharField(max_length=255)
    duration = serializers.DurationField()

    def create(self, validate_data):
        return Course.objects.create(**validate_data)

class StudentSerializer(serializers.Serializer):
    roll = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    city = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.description= validated_data.get('description',instance.description)
        instance.instructor = validated_data.get('instructor',instance.instructor)
        return instance

class EnrollmentSerializer(serializers.Serializer):
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all())
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())
    enrollment_date = serializers.DateField(read_only=True)    

    def create(self, validated_data):
        return Enrollment.objects.create(**validated_data)    