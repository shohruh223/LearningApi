from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.course.views import CourseModelViewSet, CourseLessonModelViewSet, \
    CourseCommentModelViewSet, CourseCategoryAPIView, CourserChapterAPIView, CourseChapterDetailAPIView

router = DefaultRouter()


router.register('course', CourseModelViewSet),
router.register('course-lesson', CourseLessonModelViewSet),
router.register('course-comment', CourseCommentModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('course-category/',CourseCategoryAPIView.as_view(),name='course-category'),
    path('course-chapter/',CourserChapterAPIView.as_view(),name='course-chapter'),
    path('course-chapter/<int:pk>',CourseChapterDetailAPIView.as_view(),name='course-detail')
]
