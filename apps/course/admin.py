from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.template import Origin

from apps.course.models import Course, Chapter, CourseCategory
from apps.users.models import User

admin.site.register(User, UserAdmin)
# admin.site.unregister(User)


@admin.register(CourseCategory)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    # fields = ['title', 'price', 'image']


@admin.register(Chapter)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']