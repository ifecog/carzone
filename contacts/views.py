from django.shortcuts import render, redirect
from contacts.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail

# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        user_id = request.POST['user_id']
        car_id = request.POST['car_id']
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        car_title = request.POST['car_title']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'A request has already been sent about this car. We ask  that you wait for our reply.')
                return redirect('/cars/'+car_id)

        contact = Contact(user_id=user_id, car_id=car_id, first_name=first_name, last_name=last_name, car_title=car_title,
                          customer_need=customer_need, city=city, state=state, email=email, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New Car Inquiry',
            'Hi, ' + first_name + '/nYou have a new inquiry for the car ' +
            car_title + '. Kindly login to your admin panel for more info.',
            'admin_email',
            ['ifeoluwasamson90@gmail.com'],
            fail_silently=False,
        )

        contact.save()
        messages.success(
            request, 'Your response has been submitted. We will get back to you shortly')
        return redirect('/cars/'+car_id)
