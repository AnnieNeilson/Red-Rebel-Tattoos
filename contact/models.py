from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    subject = models.CharField(max_length=80)
    body = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)


ARTIST_CHOICES = (
    ('becky', 'Becky Johnson'),
    ('alex', 'Alex Anderson'),
    ('john', 'John Masters'),
    ('alison', 'Alison Taylor'),
    ('jasmine', 'Jasmine Evans'),
    ('david', 'David Walker'),
    ('any', 'Any')
)


SUBJECT_CHOICES = (
    ('consultation', 'Free Consultation'),
    ('new', 'New Inquiry'),
    ('reschedule', 'Reschedule Appointment'),
    ('aftercare', 'Aftercare Inquiry'),
    ('other', 'Other'),
)


class Booking(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    artist = models.CharField(max_length=20, choices=ARTIST_CHOICES, default='any')
    subject = models.CharField(max_length=13, choices=SUBJECT_CHOICES, default='other')
    requested_date = models.DateField()
    message = models.TextField()
    sent = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)


class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    artist = models.CharField(max_length=20, choices=ARTIST_CHOICES, default='any')
    body = models.TextField(max_length=250)
    sent = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)    

