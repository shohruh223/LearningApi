from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.course.models import Course, Chapter, Category
from apps.users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username']


@admin.register(Category)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_filter = ['price', 'start_date', 'end_date']


@admin.register(Chapter)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
