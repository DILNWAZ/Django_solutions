from django.urls import path
from . import views

urlpatterns = [
    path('wahib/', views.wahib, name='wahib'),
]