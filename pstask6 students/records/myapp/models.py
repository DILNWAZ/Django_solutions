from django.db import models

    # Create your models here.
class Course(models.Model):
    Course_id = models.CharField(max_length=10, primary_key=True)
    title = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    instructor = models.CharField(max_length=255)
    duration = models.DurationField()

    def __str__(self):
            return self.title
        

class Student(models.Model):
        roll =models.IntegerField(unique=True, primary_key=True)
        name = models.CharField(max_length=255)
        city = models.CharField(max_length=255)

        def __str__(self):
            return self.name

    

class Enrollment(models.Model):
        student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollment')
        course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollment') 
        enrollment_date = models.DateField(auto_created=True)

        class Meta:
            unique_together = ('student', 'course')

        def __str__(self):
            return f"{self.student.name} enrolled in {self.couse.title}"        