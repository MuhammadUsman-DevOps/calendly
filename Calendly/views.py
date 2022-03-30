from datetime import datetime

from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render

from Calendly.models import Client, Service, Employee, Booking


def dashboard(request):
    total_clients = Client.objects.all().count()
    total_services = Service.objects.all().count()
    total_employees = Employee.objects.all().count()
    total_bookings = Booking.objects.all().count()

    recent_bookings = Booking.objects.filter(booking_status="In Process")

    context = {
        "total_clients": total_clients,
        "total_services": total_services,
        "total_employees": total_employees,
        "total_bookings": total_bookings,
        "recent_bookings": recent_bookings,
    }
    return render(request, template_name="administration/dashboard.html", context=context)


def services(request):
    all_services = Service.objects.all()

    if request.method == "POST":
        new_service = Service.objects.create(
            service_name=request.POST.get("service_name"),
            duration=request.POST.get("duration"),
            fee=request.POST.get("fee"),
        )
        new_service.save()

    context = {
        "services": all_services
    }
    return render(request, template_name="administration/services.html", context=context)


def employees(request):
    all_employees = Employee.objects.all()
    if request.method == "POST":
        user = User.objects.create(
            username=request.POST.get("email_address"),
            email=request.POST.get("email_address"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            is_active=True,
        )
        user.set_password(request.POST.get("password"))
        user.save()

        employee = Employee.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email_address=request.POST.get("email_address"),
            calendar_days=request.POST.get("calendar_days"),
            city=request.POST.get("city"),
            state=request.POST.get("state"),
            zip_code=request.POST.get("zip_code"),

            user=user
        )
        employee.save()

    context = {
        "employees": all_employees
    }
    return render(request, template_name="administration/employees.html", context=context)


def clients(request):
    all_clients = Client.objects.all()
    context = {
        "clients": all_clients
    }
    return render(request, template_name="administration/clients.html", context=context)


def bookings(request):
    all_bookings = Booking.objects.all()
    context = {
        "bookings": all_bookings
    }
    return render(request, template_name="administration/bookings.html", context=context)


def select_service(request, employee, name):
    all_services = Service.objects.all()
    context = {
        "services": all_services,
        "employee": employee,
        "name": name,
    }
    return render(request, template_name="booking/select-service.html", context=context)


def select_date(request, service, employee_id):
    selected_service = Service.objects.get(pk=service)
    employee = Employee.objects.get(pk=employee_id)
    restricted_dates = Booking.objects.filter(employee=employee, booking_status="In Process").last()

    context = {
        "service": selected_service,
        "employee": employee,
        "restricted_dates": restricted_dates,
    }
    return render(request, template_name="booking/select-date.html", context=context)


def confirm_booking(request, service, employee, date, slot):
    selected_service = Service.objects.get(pk=service)
    employee = Employee.objects.get(pk=employee)

    if request.method == "POST":
        case_approved = True
        client = Client.objects.create(
            client_name=request.POST.get("full_name"),
            email_address=request.POST.get("email_address"),
            phone_number=request.POST.get("phone_number"),
        )
        client.save()
        if request.POST.get("case_approved") == "None":
            case_approved = False
        formatted_date = datetime.strptime(date, "%d-%m-%Y")
        print("Date: ", formatted_date)
        new_booking = Booking.objects.create(
            service=selected_service,
            employee=employee,
            client=client,
            booking_date=formatted_date,
            booking_type=request.POST.get("booking_type"),
            booking_slot=slot,
            is_case_approved=case_approved,
            booking_status="In Process"

        )
        new_booking.save()
        messages.success(request, "Service Booked Successfully!")
    context = {
        "service": selected_service,
        "date": date,
        "slot": slot,
        "employee": employee,

    }
    return render(request, template_name="booking/confirm-booking.html", context=context)
