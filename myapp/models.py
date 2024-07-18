from django.db import models

# Create your models here.

class Contact_us(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=300)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Booking(models.Model):
    name = models.CharField(max_length=200)
    check_in = models.DateField()
    check_out = models.DateField()
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    phone_no = models.CharField(max_length=15)
    villa_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.villa_name}"


class PartnerInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.email
