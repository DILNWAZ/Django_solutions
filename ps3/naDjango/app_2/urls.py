from django.urls import path
from . import views

urlpatterns = [
    path('naDjango/', views.naDjango, name='naDjango'),
]