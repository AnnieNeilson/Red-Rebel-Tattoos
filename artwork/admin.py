from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, Contact, Booking, Review


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('caption', 'slug', 'created_on', 'status')
    search_fields = ['caption', 'description']
    prepopulated_fields = {'slug': ('caption',)}
    summernote_fields = ('description')
    list_filter = ('status', 'created_on')
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(status=1)
    
    def unpublish_posts(self, request, queryset):
        queryset.update(status=0)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'post', 'body', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name', 'subject', 'sent', 'replied')
    list_filter = ('replied',)
    search_fields = ['name', 'email', 'subject', 'artist']
    actions = ['mark_as_replied']

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):

    list_display = ('name', 'subject', 'artist', 'sent', 'replied')
    list_filter = ('replied',)
    search_fields = ['name', 'email', 'subject', 'artist']
    actions = ['mark_as_replied']

    def mark_as_replied(self, request, queryset):
        queryset.update(replied=True)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'artist', 'sent', 'approved')
    list_filter = ('approved',)
    search_fields = ['name', 'artist']
    actions = ['approve_comments']

    def approve_review(self, request, queryset):
        queryset.update(approved=True)