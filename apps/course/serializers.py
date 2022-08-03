from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SlugField
from rest_framework.serializers import Serializer, ModelSerializer, HyperlinkedModelSerializer

from apps.course.models import CourseCategory, Course, Chapter, Lesson, Comment


class CourseCategoryModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    def validated_title(self, title):
        if CourseCategory.objects.filter(title=title).exists():
            raise ValidationError('This category name already taken')

        if not title.isalpha():
            raise ValidationError('The course_category should have only chairs')

        return title

    class Meta:
        model = CourseCategory
        fields = ('id', 'title')


class CourseModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    def validate_title(self, title):
        if Course.objects.filter(title=title).exists():
            raise ValidationError('This course name already exists')

        if not title.isalpha():
            raise ValidationError('The course_name should have only chairs ')

        return title

    class Meta:
        model = Course
        fields = ('id', 'title', 'rating', 'price', 'image', 'category', 'author', 'start_date', 'end_date')


class ChapterModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    def validate_title(self, title):
        if Course.objects.filter(title=title).exists():
            raise ValidationError('This chapter title already exists')

        return title

    class Meta:
        model = Chapter
        fields = ('id', 'title', 'category')


class LessonModelSerializer(ModelSerializer):
    chapter = CharField(max_length=255)

    def validate_chapter(self, chapter):
        if Lesson.objects.filter(chapter=chapter).exists():
            raise ValidationError('This chapter lesson already exists')

        return chapter

    class Meta:
        model = Lesson
        fields = ('id', 'title', 'price', 'chapter', 'duration')


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'course')
