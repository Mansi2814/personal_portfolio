from django.contrib import admin
from django.urls import path
from mansimehndiratta import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('aboutus/', views.aboutus, name='about'),
    path('contactus/', views.contactus, name='contact'),
    path('projects/', views.projects, name='home'),
    path ('experiences/', views.experiences, name='about'),
    path('internships/', views.internships, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='signout'),
    path('otp_verification/', views.otp_verification, name='otp_verification'),
    path('profile/<str:requested_user>/', views.profile, name='profile'),
    path('add_blog/', views.add_blog, name='add_blog'),
    path('<str:blog_id>/<str:blog_title>', views.view_blog, name='view_blog'),
    path('title_img_upload/', views.title_img_view, name = 'title_img_view'),
    path('success', views.success, name = 'success'),
]
