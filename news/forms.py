from django import forms
from .models import *


class NewsForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author', 'post_category', 'title', 'text'
        ]