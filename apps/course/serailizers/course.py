from datetime import datetime
from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SlugField, HiddenField, CurrentUserDefault, DateTimeField
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
        datetime_data = datetime.strptime(represent['created_at'], '%Y-%m-%d %H:%M:%S')
        if datetime_data.year < 2021:
            orginal_datetime = datetime_data
            datetime_data = datetime_data.replace(year=2020)
            represent['created_at'] = datetime_data.strftime('%Y-%m-%d %H:%M:%S')
            represent['orginal_datetime'] = orginal_datetime
        return represent


# create
class CreateCourseModelSerializer(ModelSerializer):
    title = CharField(max_length=255)
    author = HiddenField(default=CurrentUserDefault())
    deleted_at = DateTimeField(read_only=True)

    def validate_title(self, title):
        if Course.objects.filter(title=title).exists():
            raise ValidationError('This course name already taken')

        return title

    class Meta:
        model = Course
        fields = '__all__'
        # exclude = ('type', 'is_deleted', 'deleted_at', 'updated_at')
        # read_only_fields = ['deleted_at']
        # write_only_fields = []


# Detail
class RetrieveCourseModelSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'


# put
class UpdateCourseModelSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = '__all__'

    def update(self, instance, validated_data):
        instance.course = validated_data.get('course', instance.course)
        instance.save()
        return instance


# delete
class DestroyCourseModelSerializer(ModelSerializer):

    class Meta:
        model = Course
        fields = ('id', 'title')

    def preform_destroy(self, instance):
        if instance.is_default == True:
            raise ValueError("Cannot delete default system course")
        return instance.delete()


