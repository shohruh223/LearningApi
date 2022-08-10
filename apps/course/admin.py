from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.course.models import Course, Chapter, Category
from apps.users.models import User


class ImageMixin:
    list_display = ('image', 'object_id', 'content_type')


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_filter = ['price', 'start_date', 'end_date']


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
