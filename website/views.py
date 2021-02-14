from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.


def home(request):
	return render(request, 'home.html', {})

def about(request):
	return render(request, 'about.html', {})

def services(request):
	return render(request, 'services.html', {})

def doctors(request):
	return render(request, 'doctors.html', {})

def bookings(request):
	return render(request, 'bookings.html', {})

def contact(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message_subject = request.POST['message-subject']
		message = request.POST['message']

		# send an email

		send_mail(
			message_subject, # subject
			"You have recieved this message: \n\n\n" + message + "\n\n\n from " + message_email, # message
			message_email, # from email
			['rrdentistry02@gmail.com'], # To email
			fail_silently= True,
			)

		return render(request, 'contact.html', {'message_name': message_name})

	else:
		return render(request, 'contact.html', {})

def appointment(request):
	if request.method == "POST":
		service_option_ = request.POST['service-option']
		appointment_name_ = request.POST.get('appointment_name', 'Guest (or whatever)')
		appointment_email_ = request.POST['appointment_email']
		appointment_date_ = request.POST['appointment_date']
		appointment_time_ = request.POST['appointment_time']
		phone_ = request.POST['phone']

		context = {

		'service_option_': service_option_,
		'appointment_name_': appointment_name_,
		'appointment_date_': appointment_date_,
		'appointment_time_': appointment_time_
		}


		appointment_message = " Appointment request for: \n Procedure: "+ service_option_ + "\n Time: "+ appointment_time_ +"\n Date: "+ appointment_date_ + "\n\n\n Client Information: \n Name: "+ appointment_name_ + "\n Phone: " + phone_ + "\n Email address: " + appointment_email_ + " "
		# send an email

		send_mail(
			'Appointment Request', # subject
			appointment_message, # message
			appointment_email_, # from email
			['rrdentistry02@gmail.com'], # To email
			)

		return render(request, 'appointment.html', context)

	else:
		return render(request, 'home.html', {})

