from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.course.models import Category, Course, Chapter, Lesson, Comment
from apps.course.serializers import CourseCategoryModelSerializer, CourseModelSerializer, ChapterModelSerializer, \
    LessonModelSerializer, CommentModelSerializer


class CoursePaginationAPIView(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 3
    page_size = 3


class CourseCategoryAPIView(GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CourseCategoryModelSerializer
    pagination_class = CoursePaginationAPIView

    def post(self, request):
        """
        Create category here
        """
        serializer = CourseCategoryModelSerializer(data=request.data)
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
        serializer = CourseCategoryModelSerializer(categories, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class CourseModelViewSet(ModelViewSet):
    serializer_class = CourseModelSerializer
    pagination_class = CoursePaginationAPIView
    queryset = Course.objects.all()
    lookup_url_kwarg = 'pk'
    parser_classes = (MultiPartParser,)


class CourserChapterAPIView(GenericAPIView):
    serializer_class = ChapterModelSerializer
    pagination_class = CoursePaginationAPIView
    queryset = Chapter.objects.all()
    permission_classes = (AllowAny,)
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


class CourseChapterDetailAPIView(GenericAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterModelSerializer

    def put(self, request, pk, *args, **kwargs):
        chapter = Chapter.objects.get(pk=pk)
        serializer = ChapterModelSerializer(chapter, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': "Successful update your chapter"
        }
        return Response(data)


class CourseLessonModelViewSet(ModelViewSet):
    serializer_class = LessonModelSerializer
    pagination_class = CoursePaginationAPIView
    queryset = Lesson.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (AllowAny,)


class CourseCommentModelViewSet(ModelViewSet):
    serializer_class = CommentModelSerializer
    pagination_class = CoursePaginationAPIView
    queryset = Comment.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = (AllowAny,)
