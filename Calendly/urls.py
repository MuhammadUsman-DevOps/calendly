"""Calendly URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path

from Calendly import settings, views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('services/', views.services, name="services"),
    path('employees/', views.employees, name="employees"),
    path('clients/', views.clients, name="clients"),
    path('bookings/', views.bookings, name="bookings"),

    path('select-service/<str:employee>/<str:name>/calendar/', views.select_service, name="select_service"),
    path('select-date/<int:service>/<int:employee_id>/', views.select_date, name="select_date"),
    path('confirm-booking/<int:service>/<int:employee>/<str:date>/<str:slot>/', views.confirm_booking, name="confirm_booking"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)