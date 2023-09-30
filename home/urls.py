from django.urls import path
from . import views
from django.conf import Settings


urlpatterns = [
    path('home/', views.indexView, name='home'),
    path('about/', views.aboutView, name='about'),
    path('booking/', views.bookingView, name='booking'),
    path('doctors/', views.doctorView, name='doctors'),
    path('contact/', views.contactView, name='contact'),
    path('department/', views.departmentView, name='department'),

   
]
