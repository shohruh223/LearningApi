from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import CharField, EmailField, ImageField, ManyToManyField, ForeignKey, CASCADE

from apps.shared.models import BaseModel


class CustomUserManager(BaseUserManager):

    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('Users must have a username!')

        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(username, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    INSTRUCTOR = 'teacher'
    STUDENT = 'student'
    ROLES = (
        (INSTRUCTOR, 'teacher'),
        (STUDENT, 'student')
    )
    username = CharField(max_length=255, unique=True)
    role = CharField(max_length=18, choices=ROLES)

    # reward = ManyToManyField('Reward', 'users')
    members = ManyToManyField('course.Course', 'students')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

