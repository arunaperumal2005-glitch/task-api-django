from django.contrib import admin
from django.urls import path
from .views import task_list,task_detail

urlpatterns=[
    path('task/',task_list),
    path('task/<int:pk>/',task_detail),
]