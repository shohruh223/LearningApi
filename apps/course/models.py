from django.db.models import IntegerField, Model, CharField, SlugField, ImageField, FloatField, DecimalField, \
    PositiveIntegerField, PositiveSmallIntegerField, ForeignKey, SET_NULL, CASCADE

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


class CourseModel(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=255)
    rating = IntegerRangeField(min_value=1, max_value=5)
    logo = ImageField(upload_to='course-logos/')
    image = ImageField(upload_to='course-image/')
    price = PositiveIntegerField(default=300_000)
    category = ForeignKey('CourseCategory', SET_NULL, null=True, blank=True)
    slug = SlugField(unique=True)
    author = ForeignKey('users.User', CASCADE, 'author')


class Meta:
    category = ForeignKey('CourseModel', CASCADE)
    course_duration = PositiveSmallIntegerField(default=3)
    start_date = FloatField()
    end_date = FloatField()


class Chapter(DescriptionBaseModel):
    title = CharField(max_length=255)
    category = ForeignKey(CourseModel, CASCADE)


class Lesson(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=128)
    price = DecimalField(max_digits=12, decimal_places=2)
    chapter = ForeignKey(Chapter, CASCADE, "lessons")
    duration = PositiveSmallIntegerField(default=10)
    slug= SlugField(unique=True)


class Comment(DescriptionBaseModel, DeletedModel):
    author = ForeignKey('users.User', CASCADE)
    course = ForeignKey(CourseModel, CASCADE)





