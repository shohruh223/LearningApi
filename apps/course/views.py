from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.course.models import Category, Course, Chapter, Lesson, Comment
from apps.course.serailizers.category import CategoryModelSerializer
from apps.course.serailizers.course import CreateCourseModelSerializer, ListCourseModelSerializer, \
    RetrieveCourseModelSerializer, UpdateCourseModelSerializer, DestroyCourseModelSerializer, CourseModelSerializer
from apps.course.serializers import ChapterModelSerializer, \
    LessonModelSerializer, CommentModelSerializer


# class CoursePaginationAPIView(PageNumberPagination):
#     page_size_query_param = 'page_size'
#     max_page_size = 3
#     page_size = 3


class CategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer

    # pagination_class = CoursePaginationAPIView

    def post(self, request):
        """
        Create category here
        """
        serializer = CategoryModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            success_data = {
                'message': 'Successful add your course-category'
            }
            return Response(success_data, status.HTTP_201_CREATED)

    def get(self, request, format=None):
        """
        All categories here
        """
        categories = Category.objects.all()
        serializer = CategoryModelSerializer(categories, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer
    permission_classes = (IsAuthenticated, )
    lookup_url_kwarg = 'pk'
    parser_classes = (MultiPartParser,)

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCourseModelSerializer,
            'create': CreateCourseModelSerializer,
            'retrieve': RetrieveCourseModelSerializer,
            'put': UpdateCourseModelSerializer,
            'delete': DestroyCourseModelSerializer
        }
        return serializer_dict.get(self.action, CourseModelSerializer)


# class CourseModelViewSet(ModelViewSet):
#     serializer_class = CourseModelSerializer
#     # pagination_class = CoursePaginationAPIView
#     queryset = Course.objects.all()
#     lookup_url_kwarg = 'pk'
#     parser_classes = (MultiPartParser,)


class ChapterAPIView(GenericAPIView):
    serializer_class = ChapterModelSerializer
    # pagination_class = CoursePaginationAPIView
    queryset = Chapter.objects.all()
    permission_classes = (IsAuthenticated, )
    lookup_url_kwarg = 'id'

    def post(self, request):
        serializer = ChapterModelSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            success_data = {
                'message': 'Successful add your chapter'
            }
            return Response(success_data, status.HTTP_201_CREATED)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        chapters = Chapter.objects.all()
        serializer = ChapterModelSerializer(data=chapters, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ChapterDetailAPIView(GenericAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterModelSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request, pk, *args, **kwargs):
        chapter = Chapter.objects.get(pk=pk)
        serializer = ChapterModelSerializer(chapter, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': "Successful update your chapter"
        }
        return Response(data)


class LessonModelViewSet(ModelViewSet):
    serializer_class = LessonModelSerializer
    # pagination_class = CoursePaginationAPIView
    queryset = Lesson.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticated, )


class CommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    # pagination_class = CoursePaginationAPIView
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (IsAuthenticated, )

