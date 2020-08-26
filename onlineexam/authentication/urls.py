from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('std_sign_in', views.std_sign_in, name='student_sign_in'),
    path('std_register', views.std_register, name='student_register'),
    path('tchr_sign_in', views.tchr_sign_in, name='teacher_sign_in'),
    path('tchr_register', views.tchr_register, name='teacher_register'),

]