from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.course.views import CourseCategoryModelViewSet, CourseModelViewSet, ChapterModelViewSet, LessonModelViewSet, \
    CommentModelViewSet

router = DefaultRouter()

router.register('category', CourseCategoryModelViewSet),
router.register('chapter', ChapterModelViewSet),
router.register('course', CourseModelViewSet),
router.register('lesson', LessonModelViewSet),
router.register('comment', CommentModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]
