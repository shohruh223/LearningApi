from django.urls import reverse
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class CourseTests(APITestCase):
    def test_create(self):
        url = reverse('course-list')
        data = {
            "title": "Test name"
        }
        response = self.client.post(
            url,
            data
        )
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        return response.data.get('id')
