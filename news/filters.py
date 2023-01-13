from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import *
import django_filters


class PostFilter(django_filters.FilterSet):
    added_after = DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
        model = Post
        fields = {
            'title': ['contains'],
            'author__user': ['exact'],
        }
