from django.contrib import admin
from .models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('caption', 'slug', 'created_on')
    search_fields = ['caption', 'description']
    prepopulated_fields = {'slug': ('caption',)}
    summernote_fields = ('description')
    list_filter = ('status', 'created_on')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'post', 'body', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)