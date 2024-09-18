from django.shortcuts import render
from .models import Member

# Define a function to validate an email address
import re
def is_valid_email(email):
    # Define a regular expression for validating an email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex, email) is not None

# Create your views here.
def signup(request):
    if request.method == 'POST':
        email = request.POST['email']
        full_name = request.POST['full_name']
        password = request.POST['password']
        # gender = request.POST['gender']
        P_condition = False
        E_condition = False
        if len(password) >= 8:
            P_condition = True
        if is_valid_email(email):
            E_condition = True
        if P_condition and E_condition:
            signup = Member(email=email, fullname=full_name, password=password)
            signup.save()

    return render(request, 'signup.html')