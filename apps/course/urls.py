from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.course.views import CourseModelViewSet, LessonModelViewSet, \
    CommentModelViewSet, CategoryAPIView, ChapterAPIView, ChapterDetailAPIView


router = DefaultRouter()
router.register('course', CourseModelViewSet),
router.register('lesson', LessonModelViewSet),
router.register('comment', CommentModelViewSet)
# router.register('chapter', ChapterModelViewSet)
# router.register('category-course', CategoryAPIView)

urlpatterns = [
    path('', include(router.urls)),
    path('category/',CategoryAPIView.as_view(),name='course-category'),
    path('chapter/',ChapterAPIView.as_view(),name='course-chapter'),
    path('chapter/<int:pk>', ChapterDetailAPIView.as_view(),name='course-detail')
]
