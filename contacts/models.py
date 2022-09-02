from email import message
from django.db import models
from datetime import datetime

# Create your models here.


class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    car_id = models.IntegerField()
    customer_need = models.CharField(max_length=100)
    car_title = models.CharField(max_length=100)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=15)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    date_sent = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.email
