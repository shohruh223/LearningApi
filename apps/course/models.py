from django.db.models import IntegerField, Model, CharField, SlugField, ImageField, FloatField, DecimalField, \
    PositiveIntegerField, PositiveSmallIntegerField, ForeignKey, SET_NULL, CASCADE
from django.utils.text import slugify

from apps.shared.models import DescriptionBaseModel, DeletedModel


class CourseCategory(Model):
    title = CharField(max_length=255)
    slug = SlugField(unique=True)


class IntegerRangeField(IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


class Course(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=255)
    rating = IntegerRangeField(min_value=1, max_value=5, null=True, blank=True)
    logo = ImageField(upload_to='course-logos/')
    image = ImageField(upload_to='course-images/')
    price = PositiveIntegerField(default=300_000)
    category = ForeignKey('CourseCategory', SET_NULL, null=True, blank=True)
    slug = SlugField(unique=True)
    course_duration = PositiveSmallIntegerField(default=3)
    author = ForeignKey('users.User', CASCADE, 'author')
    start_date = FloatField(null=True, blank=True)
    end_date = FloatField(null=True, blank=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Course.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        verbose_name_plural = 'Courses'


class Chapter(DescriptionBaseModel):
    title = CharField(max_length=255)
    category = ForeignKey(Course, CASCADE)


class Lesson(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=128)
    price = DecimalField(max_digits=12, decimal_places=2)
    chapter = ForeignKey(Chapter, CASCADE, "lessons")
    duration = PositiveSmallIntegerField(default=10)
    slug= SlugField(unique=True)


class Comment(DescriptionBaseModel, DeletedModel):
    author = ForeignKey('users.User', CASCADE)
    course = ForeignKey(Course, CASCADE)





