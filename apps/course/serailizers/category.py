from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from apps.course.models import Category


class CategoryModelSerializer(ModelSerializer):

    class Meta:
        model = Category
        exclude = ()


# List
class ListCategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'title')


# create
class CreateCategoryModelSerializer(ModelSerializer):
    title = CharField(max_length=255)

    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self, title):
        if Category.objects.filter(title=title).exists():
            raise ValidationError('This category name already taken')

        return title


