from django.urls import path
from . import views

urlpatterns = [

	path('', views.home, name="home"),
	path('about.html', views.about, name="about"),
	path('contact.html', views.contact, name="contact"),
	path('services.html', views.services, name="services"),
	path('doctors.html', views.doctors, name="doctors"),
	path('appointment.html', views.appointment, name="appointment"),
	path('bookings/', views.bookings, name="bookings"),





]
