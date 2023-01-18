from django import forms
from .models import *
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author', 'post_category', 'title', 'text'
        ]

class ProfileUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'email',
            'username',
        ]