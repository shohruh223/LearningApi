from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.course.views import CourseCategoryModelViewSet, CourseModelViewSet

router = DefaultRouter()
router.register('course-category', CourseCategoryModelViewSet)
router.register('course', CourseModelViewSet)

urlpatterns = [
    path('', include(router.urls))

]
