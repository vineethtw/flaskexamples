from flask.ext.testing import TestCase
import unittest

from api.api import app


class ApiTests(TestCase):
    def create_app(self):
        app.config['TESTING'] = True;
        return app;

    def test_return_hello_world(self):
        response = self.client.get('index')
        self.assert200(response)
        self.assertEquals(response.data, "Hello World!")


if __name__ == "__main__":
    unittest.main()
