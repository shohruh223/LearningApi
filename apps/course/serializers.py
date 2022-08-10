from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, SlugField, HiddenField, CurrentUserDefault
from rest_framework.serializers import Serializer, ModelSerializer, HyperlinkedModelSerializer

from apps.course.models import Category, Course, Chapter, Lesson, Comment


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
        exclude = ()


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'course')
