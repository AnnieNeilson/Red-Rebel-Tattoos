from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact, Booking, Review


# Admin controls for Contact inquiries submitted to the site.
# Includes action where inquiries can be marked as replied
@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):

    list_display = ('name', 'subject', 'sent', 'replied')
    list_filter = ('replied',)
    search_fields = ['name', 'email', 'subject', 'artist']
    actions = ['mark_as_replied']

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)


# Admin controls for Booking inquiries submitted to the site.
# Includes action where inquiries can be marked as replied
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'subject', 'artist', 'sent', 'replied')
    list_filter = ('replied',)
    search_fields = ['name', 'email', 'subject', 'artist']
    actions = ['mark_as_replied']

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)


# Admin controls for Reviews submitted to the site.
# Includes action where reviews can be marked as approved
@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'artist', 'sent', 'approved')
    list_filter = ('approved',)
    search_fields = ['name', 'artist']
    actions = ['approve_review']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)
