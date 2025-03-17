from django.urls import path
from .views import leave
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('project/', views.project, name='project'),
    path('teams/', views.teams, name='teams'),
    path('status/', views.status, name='status'),
    path('employees/', views.employees, name='employees'),
    path('leave/request/', views.leave, name='leave'),
]
