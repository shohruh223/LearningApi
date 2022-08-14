from rest_framework.exceptions import ValidationError
from rest_framework.fields import CharField, HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from apps.course.models import Comment


class CommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ()


# List
class ListCommentModelSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author')


# Create
class CreateCommentModelSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Comment
        exclude = ('deleted_at', 'is_deleted')


# Detail
class RetrieveCommentModelSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'author')


# Update
class UpdateCommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('deleted_at', 'is_deleted')


# PartialUpdate
class PartialUpdateCommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('deleted_at', 'is_deleted')


# delete
class DestroyCommentModelSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id', 'author')