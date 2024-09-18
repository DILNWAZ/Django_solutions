from django.urls import path
from . import views

urlpatterns = [
    path('relation/', views.members, name='relation'),
]