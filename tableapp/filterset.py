import django_filters
from .models import Table

class PersonFilter(django_filters.FilterSet):
    class Meta:
        model = Table
        fields = ['name', 'phone']