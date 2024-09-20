from django.http import JsonResponse
from django.views import View
from .models import Course,Student,Enrollment
from django.shortcuts import render
from .serializer import StudentSerializer,CourseSerializer,EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from django.utils.decorators import method_decorator


@method_decorator(csrf_exempt, name='dispatch')
class Course(View):
    def get(self, request, pk):
        course = Course.objects.get(id=pk)
        serializer = CourseSerializer(course)
        # json_data = JSONRenderer().render(serializer.data)
        # return HttpResponse(json_data, content_type="application/json")
        return JsonResponse(serializer.data, safe=False)
    
    def post(self, request):
        # data = request.body
        # stream = io.BytesIO(data)
        # pythonData = JSONParser().parse(stream)
        pythonData = json.loads(request.body)
        serializer = CourseSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        serializer = CourseSerializer(course, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Course updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors, status=400)

    def delete(self, request, course_id):
        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error': 'Course not found'}, status=404)
        
        
        course.delete()
        return JsonResponse({'message': 'Course deleted successfully'}, status=200)
    
class Student(View):
    def get(self, request, student_roll):
        student = Student.objects.get(roll=student_roll)
        serializer = StudentSerializer(student)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")

    def post(self, request):
        data = request.body
        stream = io.BytesIO(data)
        pythonData = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythonData)

        if serializer.is_valid():
            serializer.save()
            res = {'msg': 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, student_roll):
        try:
            student=Student.objects.get(roll=student_roll)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status =404)
        
        try:
            data = json.loads(request.body)
        except:
            return JsonResponse({'error': 'Invalid data'}, status=400)
        
        serializer = StudentSerializer(student, data=data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'message': 'Student updated successfully'}, status= 200)
        else:
            return JsonResponse(serializer.errors, status=400)
    
    def delete(self, request, student_roll):
        try:
            student = Student.objects.get(roll=student_roll)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        
        student.delete()
        return JsonResponse({'message': 'Student deleted successfully'}, status=200)