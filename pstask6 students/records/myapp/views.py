from django.shortcuts import render
from .models import Student,Course,Enrollment
from .serializer import CourseSerializer,StudentSerializer,EnrollmentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
import io
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

def course_detail(request,course_id):
   print(course_id)
   stu = Course.objects.get(course_id=course_id)
   serializer = CourseSerializer(stu)
   json_data = JSONRenderer().render(serializer.data)
   return HttpResponse(json_data, content_type="application/json")

def course_list(request):
    stu = Course.objects.all()
    serializer = CourseSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type="application/json")

def get_all_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    else:
        return HttpResponse(status=405)
    
def get_student_by_course(request, course_id):
    print(course_id)
    if request.method == 'GET':
        try:
         course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
         return HttpResponse(JSONRenderer().render({'error':'course not found'}), content_type="application/json")
        enrollments = Enrollment.objects.filter(course=course)
        students = [enrollment.student for enrollment in enrollments]
        serializer = StudentSerializer(students, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data ,content_type="application/json")
    else:
       return HttpResponse(status=405)
    
def get_specific_student_in_course(request, course_id, student_roll):
    if request.metod == 'GET':
        try:
           course = Course.objects.get(course_id=course_id)
           student = Student.objects.get(roll=student_roll)
           enrollment = Enrollment.objects.get(course=course, student=student)
        except Course.DoesNotExist:
           return HttpResponse(JSONRenderer().render({'error': 'Course not found'}),content_type="application/json")
        except Student.DoesNotExist:
           return HttpResponse(JSONRenderer().render({'error': 'Course not found'}),content_type="application/json")     
        except Enrollment.DoesNotExist:
           return HttpResponse(JSONRenderer().render({'error': 'Student is not enrolled'}),content_type="application/json")
        
        serializer = StudentSerializer(student)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type="application/json")
    else:
       return HttpResponse(status=405)
   

@csrf_exempt
def stu_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json")  
          
@csrf_exempt
def course_create(request):
    if request.method == "POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer1 = CourseSerializer(data = pythondata)
        print('out of serailizer')
        if serializer1.is_valid():
          print('in serailizer.....')
          serializer1.save()
          res = {"msg" : "Data created"}
          json_data = JSONRenderer().render(res)
          return HttpResponse(json_data, content_type = "application/json")
    json_data = JSONRenderer().render(serializer1.error_messages)
    return HttpResponse(json_data, content_type = "application/json")
    
@csrf_exempt
def enroll(request):
    if request.method == "POST":
        data = request.body
        stream = io.BytesIO(data)
        pythondata = JSONParser().parse(stream)
        course_id = pythondata["course"]
        student_id = pythondata["student"]
        try:
            course = Course.objects.get(course_id = course_id)
        except Course.DoesNotExist:
            return HttpResponse(JSONRenderer().render({"Error" : "Course does not found"}), content_type='application/json')
      
        try:
            student = Student.objects.get(roll = student_id)
        except Course.DoesNotExist:
            return HttpResponse(JSONRenderer().render({"Error" : "Student does not found"}), content_type='application/json')
      
        serializer = EnrollmentSerializer(data = pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : "Data created"}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.error_messages)
        return HttpResponse(json_data, content_type = "application/json")
    
@csrf_exempt
def delete_course(request, course_id):
    if request.method == 'DELETE':
        try :
            course = Course.objects.get(course_id=course_id)
        except Course.DoesNotExist:
            return JsonResponse({'error':'Course not found'}, status=404)

        course.delete()
        return JsonResponse({'message':'course deletes successfully'},status=200)

    return HttpResponse(status=405)

@csrf_exempt
def update_student(request, student_roll):
    if request.method == 'PUT':
        try:
            student = Student.objects.get({'error':'Student not found'},status=404)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Student not found'},status=400)
        
        try:
            data = json.loads(request.bodty)
        except   json.JSONDecoderError: 
            return JsonResponse({'error':'invalid Json'},status=400)
        
        serializer = StudentSerializer(student, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'messae':'Student updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors,status=400)
        
    return HttpResponse(status=405)

@csrf_exempt
def delete_student(request, student_roll):
    if request.method == 'DELETE':
        try :
            course = Student.objects.get(roll=student_roll)
        except Student.DoesNotExist:
            return JsonResponse({'error':'Course not found'}, status=404)

        course.delete()
        return JsonResponse({'message':'course deletes successfully'},status=200)

    return HttpResponse(status=405)

@csrf_exempt
def update_course(request, course_id):
    if request.method == 'PUT':
        try:
            course = Course.objects.get({'error':'Student not found'},status=404)
        except Course.DoesNotExist:
            return JsonResponse({'error':'Student not found'},status=400)
        
        try:
            data = json.loads(request.bodty)
        except   json.JSONDecoderError: 
            return JsonResponse({'error':'invalid Json'},status=400)
        
        serializer = CourseSerializer(course, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'messae':'Student updated successfully'}, status=200)
        else:
            return JsonResponse(serializer.errors,status=400)
        
    return HttpResponse(status=405)