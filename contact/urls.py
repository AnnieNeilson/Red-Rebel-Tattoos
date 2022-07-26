from django.urls import path
from . import views


urlpatterns = [
    path('contact', views.ContactPage.as_view(), name='contact'),
    path('booking', views.BookingPage.as_view(), name='booking'),
]