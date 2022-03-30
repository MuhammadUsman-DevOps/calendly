from django.contrib.auth.models import User
from django.db import models


class Service(models.Model):
    service_name = models.CharField(max_length=500)
    duration = models.CharField(max_length=100, null=True, blank=True)
    fee = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    email_address = models.EmailField(null=True, blank=True)
    calendar_days = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.first_name

    class Meta:
        verbose_name = "Employees"
        verbose_name_plural = "Employees"


class Client(models.Model):
    client_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    phone_number = models.CharField(max_length=100, null=True, blank=True)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name

    class Meta:
        verbose_name = "Client"
        verbose_name_plural = "Clients"


class Booking(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    booking_date = models.DateField()
    booking_type = models.CharField(max_length=100)
    booking_slot = models.CharField(max_length=100)
    is_case_approved = models.BooleanField(default=False)
    booking_status = models.CharField(max_length=100)

    active = models.BooleanField(default=True)

    def __str__(self):
        return self.employee.first_name

    class Meta:
        verbose_name = "Bookings"
        verbose_name_plural = "Bookings"
