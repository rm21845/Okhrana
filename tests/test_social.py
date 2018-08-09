"""
import unittest
from app.models.social import Social


class SocialTestCase(unittest.TestCase):
    def setUp(self):
        self.sc = Social()

    def test_byusername0(self):
        self.assertIsNotNone(self.sc.by_username('johnsmith'))

    def test_byusername1(self):
        self.assertIsNotNone(self.sc.by_username('rm21845'))

    def test_byusername2(self):
        self.assertIsNotNone(self.sc.by_username('discorduser'))
        """