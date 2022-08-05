from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.course.models import Category, Course, Chapter, Lesson, Comment
from apps.course.serializers import CourseCategoryModelSerializer, CourseModelSerializer, ChapterModelSerializer, \
    LessonModelSerializer, CommentModelSerializer


class CourseCategoryModelViewSet(ModelViewSet):
    serializer_class = CourseCategoryModelSerializer
    queryset = Category.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = ()

    # def create(self, request, *args, **kwargs):
    #     serializer = CourseCategoryModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = {'message': 'Successful add your category'}
    #     return Response(data=data, status=status.HTTP_201_CREATED)
    #
    # def list(self, request, *args, **kwargs):
    #     categories = Category.objects.all()
    #     serializer = CourseCategoryModelSerializer(data=categories, many=True)
    #     return Response(data=serializer.data)


class CourseModelViewSet(ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser,)

    # def create(self, request, *args, **kwargs):
    #     serializer = CourseModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = {
    #         'message': 'Successful add you course'
    #     }
    #     return Response(data=data, status=status.HTTP_201_CREATED)
    #
    # def list(self, request, *args, **kwargs):
    #     courses = Course.objects.all()
    #     serializer = CourseModelSerializer(data=courses, many=True)
    #     return Response(data=serializer.data)


class ChapterModelViewSet(ModelViewSet):
    serializer_class = ChapterModelSerializer
    queryset = Chapter.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = ()


class LessonModelViewSet(ModelViewSet):
    serializer_class = LessonModelSerializer
    queryset = Lesson.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = ()


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = ()
