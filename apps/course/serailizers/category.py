from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.course.models import Category


class CategoryModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    def validated_title(self, title):
        if Category.objects.filter(title=title).exists():
            raise ValidationError('This category name already taken')

        return title

    class Meta:
        model = Category
        exclude = ()

