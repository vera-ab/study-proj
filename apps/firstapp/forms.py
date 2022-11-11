from django import forms

from .models import User


class PostForm(forms.Form):
    name = forms.CharField()
    post = forms.CharField(widget=forms.Textarea)
