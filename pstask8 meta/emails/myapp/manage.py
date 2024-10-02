from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.contrib.auth.base_user import BaseUserManager

# Custom User Manager
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password=None, **extra_field):
        #create and saves a user with the given email and password
        if not email:
            raise ValueError('the given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_field) 
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password=None, **extra_fields):
        # create a reggular user
        extra_fields.setdefault('is_staff',False)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,password, **extra_fields)
    
    def create_superuser(self, email, password=None, **extra_fields):
        # create asuperuser
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('superuser must have is_superuser=True.')
        