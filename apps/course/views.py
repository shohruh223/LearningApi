from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.course.models import Category, Course, Chapter, Lesson, Comment
from apps.course.serailizers.category import CategoryModelSerializer
from apps.course.serailizers.chapter import ChapterModelSerializer
from apps.course.serailizers.comment import ListCommentModelSerializer, CreateCommentModelSerializer, \
    RetrieveCommentModelSerializer, UpdateCommentModelSerializer, PartialUpdateCommentModelSerializer, \
    DestroyCommentModelSerializer, CommentModelSerializer
from apps.course.serailizers.course import CreateCourseModelSerializer, ListCourseModelSerializer, \
    RetrieveCourseModelSerializer, UpdateCourseModelSerializer, DestroyCourseModelSerializer, CourseModelSerializer, \
    PartialUpdateCourseModelSerializer
from apps.course.serailizers.lesson import LessonModelSerializer, ListLessonModelSerializer, \
    DestroyLessonModelSerializer, PartialUpdateLessonModelSerializer, CreateLessonModelSerializer, \
    RetrieveLessonModelSerializer, UpdateLessonModelSerializer


class CategoryAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        """
        Create category here
        """
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class CourseModelViewSet(ModelViewSet):
    queryset = Course.objects.order_by('id')
    serializer_class = CourseModelSerializer
    permission_classes = (IsAuthenticated, )
    parser_classes = (MultiPartParser,)

    # def get_serializer_class(self):
    #     if self.action == 'create':
    #         return CreateCourseModelSerializer
    #     elif self.action == 'list':
    #         return ListCourseModelSerializer
    #     elif self.action == 'retrieve':
    #         return RetrieveCourseModelSerializer
    #     elif self.action == 'update':
    #         return UpdateCourseModelSerializer
    #     elif self.action == 'partial_update':
    #         return PartialUpdateCourseModelSerializer
    #     elif self.action == 'destroy':
    #         return DestroyCourseModelSerializer
    #     return super().get_serializer_class()

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCourseModelSerializer,
            'create': CreateCourseModelSerializer,
            'retrieve': RetrieveCourseModelSerializer,
            'update': UpdateCourseModelSerializer,
            'partial_update': PartialUpdateCourseModelSerializer,
            'destroy': DestroyCourseModelSerializer
        }
        return serializer_dict.get(self.action, CourseModelSerializer)


class ChapterAPIView(GenericAPIView):
    serializer_class = ChapterModelSerializer
    queryset = Chapter.objects.all()
    permission_classes = (IsAuthenticated, )
    lookup_url_kwarg = 'id'

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        success_data = {
                'message': 'Successful add your chapter'
            }
        return Response(success_data, status.HTTP_201_CREATED)

    def get(self, request):
        chapters = self.queryset
        serializer = self.serializer_class(data=chapters, many=True)
        return Response(serializer.data, status.HTTP_200_OK)


class ChapterDetailAPIView(GenericAPIView):
    queryset = Chapter.objects.all()
    serializer_class = ChapterModelSerializer
    permission_classes = (IsAuthenticated, )

    def put(self, request, pk, *args, **kwargs):
        chapter = Chapter.objects.get(pk=pk)
        serializer = self.serializer_class(chapter, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {
            'message': "Successful update your chapter"
        }
        return Response(data)


class LessonModelViewSet(ModelViewSet):
    queryset = Lesson.objects.order_by('id')
    serializer_class = LessonModelSerializer
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListLessonModelSerializer,
            'create': CreateLessonModelSerializer,
            'retrieve': RetrieveLessonModelSerializer,
            'update': UpdateLessonModelSerializer,
            'partial_update': PartialUpdateLessonModelSerializer,
            'destroy': DestroyLessonModelSerializer
        }
        return serializer_dict.get(self.action, LessonModelSerializer)


class CommentModelViewSet(ModelViewSet):
    queryset = Comment.objects.order_by('id')
    serializer_class = CommentModelSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        serializer_dict = {
            'list': ListCommentModelSerializer,
            'create': CreateCommentModelSerializer,
            'retrieve': RetrieveCommentModelSerializer,
            'update': UpdateCommentModelSerializer,
            'partial_update': PartialUpdateCommentModelSerializer,
            'destroy': DestroyCommentModelSerializer
        }
        return serializer_dict.get(self.action, CommentModelSerializer)
