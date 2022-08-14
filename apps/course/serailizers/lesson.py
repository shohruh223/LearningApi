from rest_framework.serializers import ModelSerializer
from apps.course.models import Lesson


class LessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        exclude = ()


# List
class ListLessonModelSerializer(ModelSerializer):

    class Meta:
        model = Lesson
        fields = ('id', 'title')


# Create
class CreateLessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('deleted_at', 'is_deleted')


# Retrieve
class RetrieveLessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title')


# Update
class UpdateLessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('deleted_at', 'is_deleted')


# PartialUpdate
class PartialUpdateLessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        exclude = ('deleted_at', 'is_deleted')


# Destroy
class DestroyLessonModelSerializer(ModelSerializer):
    class Meta:
        model = Lesson
        fields = ('id', 'title')