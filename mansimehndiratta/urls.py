from django.contrib import admin
from django.urls import path
from mansimehndiratta import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path ('aboutus/', views.aboutus, name = 'about'),
    path('contactus/', views.contactus, name = 'contact'),
    path('projects/', views.projects, name = 'home'),
    path ('experiences/', views.experiences, name = 'about'),
    path('internships/', views.internships, name = 'contact')
] 