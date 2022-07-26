from django.shortcuts import render
from django.views import View
from .models import Review
from .forms import ContactForm, BookingForm, ReviewForm


class HomePage(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        reviews = Review.objects.filter(approved=True)
        return render(
            request,
            "index.html",
            {
                "reviews": reviews,
            },)


class BookingPage(View):
    template_name = 'booking.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "booking.html",
            {
                "booking_form": BookingForm(),
            },)

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking_form.instance.email = request.user.email
            booking_form.instance.name = request.user.username
            booking_form.save()
            return render(request, 'booking_successful.html',)
        else:
            booking_form = BookingForm()
            return render(
                request,
                "booking.html",
                {
                    "booking_form": BookingForm(),
                },)


class ContactPage(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            "contact.html",
            {
                "contact_form": ContactForm(),
                "review_form": ReviewForm(),
                "reviewed" : False,
            },)

    def post(self, request, *args, **kwargs):
        if 'contact' in request.POST:
            contact_form = ContactForm(data=request.POST)
            if contact_form.is_valid():
                contact_form.save() 
                return render(request, 'contact_successful.html',)
        elif 'review' in request.POST:
            review_form = ReviewForm(data=request.POST)
            if review_form.is_valid():
                review_form.instance.email = request.user.email
                review_form.instance.name = request.user.username
                review_form.save() 
                return render(
                    request,
                    "contact.html",
                    {
                        "contact_form": ContactForm(),
                        "review_form": ReviewForm(),
                        "reviewed" : True,
                    },)
        else:
            contact_form = ContactForm()
            review_form = ReviewForm()
            return render(
                request,
                "contact.html",
                {
                    "contact_form": ContactForm(),
                    "review_form": ReviewForm(),
                },)
