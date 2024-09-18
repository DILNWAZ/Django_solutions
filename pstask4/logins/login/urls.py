from django.urls import path
from . import views

urlpatterns = [
    # path('home/',view.home , name='home')
    # path('login/',view.logins , name='login')
    path('signup/',views.signup , name='signup')
]