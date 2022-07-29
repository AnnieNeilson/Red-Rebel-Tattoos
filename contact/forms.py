from django import forms
from .models import Contact, Booking, Review


# Form for users, validated or not, to contact the staff/site admin
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body']


# Form for validated users to post a review to staff/admin
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['artist', 'review']


# Date input for booking form
class DateInput(forms.DateInput):
    input_type = 'date'


# Form for validated users to make booking etc. inquiries to staff/admin
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['artist', 'subject', 'requested_date', 'message']
        widgets = {
            'requested_date': DateInput()
        }
