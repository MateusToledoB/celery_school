from django.contrib import admin
from django.urls import path, include
from .views import StudentCreateView, StudentListView

urlpatterns = [
    path('', StudentListView.as_view(), name='student-list'),
    path('create/', StudentCreateView.as_view(), name='student-create'),
]