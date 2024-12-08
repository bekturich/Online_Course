from django_filters import FilterSet
from .models import Course


class CourserFilter(FilterSet):
    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
            'price': ['gt', 'lt'],
        }
