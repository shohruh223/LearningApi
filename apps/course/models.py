from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import IntegerField, Model, CharField, SlugField, ImageField, FloatField, DecimalField, \
    PositiveIntegerField, PositiveSmallIntegerField, ForeignKey, SET_NULL, CASCADE, DateField
from django.utils.text import slugify

from apps.shared.models import DescriptionBaseModel, DeletedModel


class Category(Model):
    title = CharField(max_length=255)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Course.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'
        db_table = 'category'


class Course(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=255)
    rating = IntegerField(
        validators=[
            MaxValueValidator(5, 'The highest mark is 5'),
            MinValueValidator(2, 'The minimum mark is 2')
        ], default=3
    )
    logo = ImageField(upload_to='course-logos/', null=True, blank=True)
    image = ImageField(upload_to='course-image/', null=True, blank=True)
    price = PositiveIntegerField(default=300_000)
    category = ForeignKey('Category', SET_NULL, null=True, blank=True)
    course_duration = PositiveSmallIntegerField(default=3)
    author = ForeignKey('users.User', CASCADE, 'author', null=True, blank=True)
    start_date = DateField(null=True, blank=True)
    end_date = DateField(null=True, blank=True)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Course.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'

        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Courses'
        db_table = 'course'


class Chapter(DescriptionBaseModel):
    title = CharField(max_length=255)
    category = ForeignKey(Course, CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Chapters'
        db_table = 'chapter'


class Lesson(DescriptionBaseModel, DeletedModel):
    title = CharField(max_length=128)
    price = DecimalField(max_digits=12, decimal_places=2)
    chapter = ForeignKey(Chapter, CASCADE, "lessons")
    duration = PositiveSmallIntegerField(default=10)
    slug = SlugField(unique=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.slug:
            self.slug = slugify(self.title)
            while Lesson.objects.filter(slug=self.slug).exists():
                self.slug = f'{self.slug}-1'
        super().save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Lessons'
        db_table = 'lesson'


class Comment(DescriptionBaseModel, DeletedModel):
    author = ForeignKey('users.User', CASCADE)
    course = ForeignKey(Course, CASCADE)

    def __str__(self):
        return f'{self.author.username}:{self.course}:{self.text}'

    class Meta:
        verbose_name_plural = 'Comments'
        db_table = 'comment'
