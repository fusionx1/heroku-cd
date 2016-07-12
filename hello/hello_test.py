import unittest

from .hello_app import app


class HelloTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_root(self):
        assert '<h1>Hello' in self.app.get('/').data
