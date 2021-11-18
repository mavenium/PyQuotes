from http import HTTPStatus
from django.test import TestCase


class TestIndex(TestCase):
    def test_get_admin_returns_200(self):
        response = self.client.get('/')
        assert response.status_code == HTTPStatus.OK, response
