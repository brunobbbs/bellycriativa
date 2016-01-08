from django.test import TestCase


class HomePageTest(TestCase):

    def setUp(self):
        self.resp = self.client.get('/')

    def test_homepage_get(self):
        self.assertEqual(200, self.resp.status_code)