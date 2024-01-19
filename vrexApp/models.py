# models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django import forms
from datetime import date



class CustomUser(AbstractUser):
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    middle_name = models.CharField(_("middle name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    GENDER_CHOICES = [
        ('', 'Choose Gender'),
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    sex = models.CharField(_("sex"), max_length=10, choices=GENDER_CHOICES, blank=True)
    USER_TYPE_CHOICES = [
        ('', 'Choose User Type'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    user_type = models.CharField(_("user type"), max_length=10, choices=USER_TYPE_CHOICES, blank=True)
    home_address = models.CharField(_("home address"), max_length=150, blank=True)
    contact_number = models.CharField(
        _("contact number"),
        max_length=150,
        blank=True,
        validators=[
            RegexValidator(
                regex=r'^\+63\d{10}$',
                message=_("Enter a valid cellphone number starting with +63."),
            ),
        ],
        help_text=_("Enter a valid cellphone number starting with +63."),
    )

    def __str__(self):
        return self.username



class SchoolForm(models.Model):
    first_name = models.CharField(_("first name"), max_length=150)
    middle_name = models.CharField(_("middle name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150)
    
    
    USER_TYPE_CHOICES = [
        ('', 'Choose User Type'),
        ('student', 'Student'),
        ('parent', 'Parent'),
    ]
    user_type = models.CharField(_("Role"), max_length=10, choices=USER_TYPE_CHOICES)
    purpose = models.TextField(_("Purpose of Request"), max_length=150, blank=True)
    
    REQUEST_CHOICES = [
        ('', 'What are you requesting?'),
        ('f137', 'F137'),
        ('coe', 'COE'),
    ]
    requestform = models.CharField(_("Forms"), max_length=10, choices=REQUEST_CHOICES)
    request_date = models.DateField(_("Request Date"), default=date.today)
    specialinstructions = models.TextField(_("Special Instructions"), max_length=150, blank=True)
    
    STATUS_CHOICES = [
        ('Ongoing', 'Ongoing'),
        ('Completed', 'Completed'),
    ]
    status = models.CharField(_("status"), max_length=10, choices=STATUS_CHOICES, default='Ongoing')
    date_released = models.DateTimeField(_("date released"), blank=True, null=True)
    
    # New field to store the user who made the request
    requested_by = models.ForeignKey(CustomUser(), on_delete=models.CASCADE, related_name='school_forms', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.requestform} - Requested by: {self.requested_by}"
    
    @classmethod
    def total_request_count(cls):
        return cls.objects.count()

    @classmethod
    def ongoing_request_count(cls):
        return cls.objects.filter(status='Ongoing').count()

    @classmethod
    def monthly_document_requests(cls):
        from django.db.models import Count
        return cls.objects.filter(status='Completed').extra(
            {'month': "EXTRACT(month FROM date_released)", 'year': "EXTRACT(year FROM date_released)"}
        ).values('month', 'year').annotate(count=Count('id'))

    @classmethod
    def recent_actions(cls, limit=5):
        return cls.objects.filter(status='Completed').order_by('-date_released')[:limit]
    
    def save(self, *args, **kwargs):
        # Set requested_by to the currently logged-in user when saving the form
        user = kwargs.pop('user', None)
        if user and self.requested_by is None:
            self.requested_by = user
        super().save(*args, **kwargs)    
    
    
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    recipient = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.sender} to {self.recipient} - {self.timestamp}'
    

class Report(models.Model):
    title = models.CharField(_("Title"), max_length=150)
    content = models.TextField(_("Content"))
    created_at = models.DateTimeField(_("Created At"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated At"), auto_now=True)

    def __str__(self):
        return self.title