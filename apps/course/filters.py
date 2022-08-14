from django_filters import FilterSet

from apps.course.models import Course


class CourseFilter(FilterSet):

    class Meta:
        model = Course
        fields = ('title', )
