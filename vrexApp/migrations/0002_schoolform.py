# Generated by Django 4.2.9 on 2024-01-16 06:13

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vrexApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=150, verbose_name='middle name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('sex', models.CharField(blank=True, choices=[('', 'Choose Gender'), ('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=10, verbose_name='sex')),
                ('user_type', models.CharField(blank=True, choices=[('', 'Choose User Type'), ('student', 'Student'), ('parent', 'Parent')], max_length=10, verbose_name='user type')),
                ('home_address', models.CharField(blank=True, max_length=150, verbose_name='home address')),
                ('contact_number', models.CharField(blank=True, help_text='Enter a valid cellphone number starting with +63.', max_length=150, validators=[django.core.validators.RegexValidator(message='Enter a valid cellphone number starting with +63.', regex='^\\+63\\d{10}$')], verbose_name='contact number')),
            ],
        ),
    ]