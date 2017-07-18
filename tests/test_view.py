import unittest
from landingpage.main import app

class TestView(unittest.TestCase):
        def setUp(self):
            app.config['TESTING'] = True
            self.app = app.test_client()

        def tearDown(self):
            pass

        def test_sanity(self):
            self.assertEqual(2, 2)

        def test_home_status_code(self):
            result = self.app.get('/')
            self.assertEqual(result.status_code, 200)
