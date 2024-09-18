from django.shortcuts import render
from .models import Students
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import io

# Create your views here.

def Student_details(request,pk):
    stu = Students.objects.get(id = pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

def studentinfo(request):
    stu = Students.objects.all()
    serializer = StudentSerializer(stu, many = True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type = "application/json")

@csrf_exempt
def  Student_create(request):
    if request.method == 'POST':
        json_data = request.body
        print(json_data)
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type="application/json")
        json_data = JSONRenderer().render(serializer.error_message)
        return HttpResponse(json_data, content_type="application/json")