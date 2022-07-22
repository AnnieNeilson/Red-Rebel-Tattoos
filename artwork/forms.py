from django import forms
from .models import Comment, Contact, Booking


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'body']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['artist', 'subject', 'date', 'message']