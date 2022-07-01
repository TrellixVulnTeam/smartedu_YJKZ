import django_filters
from .models import *

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = Course
        fields=['user', 'title','university','major_types','category']