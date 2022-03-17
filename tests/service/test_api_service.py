
from unittest import TestCase
from unittest.mock import patch, Mock, MagicMock

from Service.ApiService import ApiService


class MockService(ApiService):

    @property
    def dao(self):
        return Mock()

    @property
    def schema(self):
        return Mock()


class TestApiService(TestCase):

    service_mock = MockService()

    def test_get_all(self):
        self.service_mock.get_all()



