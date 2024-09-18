from django.db import models

class Member(models.Model):
    email = models.EmailField()
    fullname = models.CharField(max_length=255)
    password = models.CharField(max_length=110)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
      return f"{self.fullname} {self.password}"
