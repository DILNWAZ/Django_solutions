from django.contrib import admin
from .models import Student,Course, Enrollment

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'name', 'city')
    search_fields = ('roll', 'name', 'city')
    ordering = ('roll',)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'duration')
    search_fields = ('title', 'instructor')
    ordering = ('title',)

@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'enrollment_date')
    search_fields = ('student__name', 'course__title')
    list_filter = ('course',)
    ordering = ('enrollment_date',)

