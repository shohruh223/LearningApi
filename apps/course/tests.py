from django.contrib.auth.models import User
from rest_framework import test, status
from rest_framework.reverse import reverse

from apps.course.models import CourseModel

login = 'admin'
password = '1'


class CategoryTestCase(test.APITestCase):
    fixtures = [
        'category.json'
    ]

    def setUp(self):
        User.objects.create_user(
            username=login,
            password=password
        )
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.get_token())

    def _authenticate(self, login: str, password: str):
        url = reverse('token')
        data = {
            "username": login,
            "password": password
        }
        token = self.client.post(url, data)
        return token

    def get_token(self, username=login, password=password) -> str:
        token = self._authenticate(username, password)
        return token.data.get('token', None)

    def test_create(self):
        url = reverse('course-list')
        data = {
            "name": "Test name"
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        return response.data.get('id')

    def test_get_pk(self):
        pk = self.test_create()
        url = reverse('category-detail', kwargs={"pk": pk})
        response = self.client.get(url)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        return response.data.get('id')

    def test_get_list(self):
        url = reverse('category-list')
        response = self.client.get(url)

        self.assertEquals(status.HTTP_200_OK, response.status_code)
        self.assertEquals(CourseModel.objects.count(), 4)

    def test_update(self):
        pk = self.test_get_pk()
        url = reverse('course-detail', kwargs={"pk": pk})

        data = {
            "name": "Test name 2",
        }

        response = self.client.put(url, data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_delete(self):
        pk = self.test_get_pk()
        url = reverse('category-detail', kwargs={"pk": pk})
        response = self.client.delete(url)
        self.assertEquals(status.HTTP_204_NO_CONTENT, response.status_code)

