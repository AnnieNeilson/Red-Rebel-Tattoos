from django import forms
from .models import Contact, Booking, Review

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['artist', 'body',]


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['artist', 'subject', 'requested_date', 'message']
        widgets = {
            'requested_date': DateInput()
        }