# Generated by Django 3.2.12 on 2022-03-30 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calendly', '0002_booking_booking_slot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='booking_date',
            field=models.DateField(),
        ),
    ]
