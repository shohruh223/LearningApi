from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.course.models import CourseCategory, Course
from apps.course.serializers import CourseCategoryModelSerializer, CourseModelSerializer


class CourseCategoryModelViewSet(ModelViewSet):
    serializer_class = CourseCategoryModelSerializer
    queryset = CourseCategory.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (AllowAny,)

    # def create(self, request, *args, **kwargs):
    #     serializer = CourseCategoryModelSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     data = {'message': 'Successful add your category'}
    #     return Response(data=data, status=status.HTTP_201_CREATED)
    #
    # def list(self, request, *args, **kwargs):
    #     categories = CourseCategory.objects.all()
    #     serializer = CourseCategoryModelSerializer(data=categories, many=True)
    #     return Response(data=serializer.data)


class CourseModelViewSet(ModelViewSet):
    serializer_class = CourseModelSerializer
    queryset = Course.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (AllowAny,)
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
