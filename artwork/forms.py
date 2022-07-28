from django import forms
from .models import Comment


# Form for validated users to make comments of a specific post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
