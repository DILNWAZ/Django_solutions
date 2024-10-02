from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manage import UserManager
# Create your models here.
class User(AbstractBaseUser):
    username = None
    email = models.EmailField(umique = True)
    is_varified = models.BooleanField(default = False)
    otp = models.CharField(max_length=6, null=True, blank= True)
    USERNAME_FIELD = 'email'
    object = UserManager()
    def name(self):
        return self.first +''+self.last_name
    def __str__(self):
        return self.email
