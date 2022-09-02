from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages

# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by(
        '-created_date').filter(is_featured=True)
    latest_cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    data = {
        'teams': teams,
        'features': featured_cars,
        'latest': latest_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    return render(request, 'pages/about.html')


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + \
            '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=False)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            message_body,
            'ifeoluwasamson90@gmail.com',
            [admin_email],
            fail_silently=False,
        )

        messages.success(
            request, 'Your message has been successfully sent. We would get back to you shortly.')
        return redirect('contact')

    return render(request, 'pages/contact.html')
