from datetime import datetime

from django.db.models import ForeignKey, CASCADE
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SlugField, HiddenField, CurrentUserDefault, DateTimeField, IntegerField
from rest_framework.serializers import Serializer, ModelSerializer, HyperlinkedModelSerializer
from apps.course.models import Category, Course, Chapter, Lesson, Comment


class CourseModelSerializer(ModelSerializer):

    class Meta:
        model = Course
        exclude = ()


# List
class ListCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'create_at')

    def to_representation(self, instance):
        represent = super().to_representation(instance)
        datetime_data = datetime.strptime(represent['create_at'], '%Y-%m-%d %H:%M:%S')
        if datetime_data.year < 2021:
            orginal_datetime = datetime_data
            datetime_data = datetime_data.replace(year=2020)
            represent['create_at'] = datetime_data.strftime('%Y-%m-%d %H:%M:%S')
            represent['orginal_datetime'] = orginal_datetime
        return represent


# create
class CreateCourseModelSerializer(ModelSerializer):
    title = CharField(max_length=255)
    author = HiddenField(default=CurrentUserDefault())

    def validated_title(self, title):
        if Course.objects.filter(title=title).exists():
            raise ValidationError('This category name already taken')

        return title

    class Meta:
        model = Course
        exclude = ('deleted_at', 'is_deleted')


# Detail
class RetrieveCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')


# put
class UpdateCourseModelSerializer(ModelSerializer):
    title = CharField(max_length=255, required=False)
    # slug = SlugField(required=True)

    class Meta:
        model = Course
        exclude = ('deleted_at', 'is_deleted')


#patch
class PartialUpdateCourseModelSerializer(ModelSerializer):
    title = CharField(max_length=255, required=False)
    # slug = SlugField(required=True)

    class Meta:
        model = Course
        exclude = ('deleted_at', 'is_deleted')
        read_only_fields = ('start_of_working_day', 'end_of_working_day')


# delete
class DestroyCourseModelSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title')



