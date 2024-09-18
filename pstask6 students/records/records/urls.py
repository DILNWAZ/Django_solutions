from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<str:course_id>', views.course_detail, name='course_details'),
    path('students/', views.get_all_students, name='get_all_students'),
    path('courses/<str:course_id>/students', views.get_student_by_course, name='get_student_by_course'),
    path('courses/<str:course_id>/students/<int:student_roll>', views.get_specific_student_in_course, name='get_specific_student_in_course'),
    path('stu_create/', views.stu_create, name='stu_create'),
    path('course_create/', views.course_create, name='course_create'),
]
