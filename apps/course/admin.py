from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.template import Origin

from apps.course.models import Course, Chapter
from apps.users.models import User

admin.site.register(User, UserAdmin)
# admin.site.unregister(User)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'price']
    fields = ['title', 'price', 'image']

