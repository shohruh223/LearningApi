from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer
from apps.course.models import Course, Chapter


class ChapterModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    def validated_title(self, title):
        if Course.objects.filter(title=title).exists():
            raise ValidationError('This chapter title already exists')

        return title

    class Meta:
        model = Chapter
        exclude = ()




