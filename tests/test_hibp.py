import unittest
from app.models.hibp import hibp


class HaveIBPTestCase(unittest.TestCase):
    def setUp(self):
        self.pwned = hibp()

    def test_breaches(self):
        self.assertIsNotNone(self.pwned.breaches('johnsmith'))

    def test_pastes0(self):
        self.assertIsNotNone(self.pwned.pastes('johnsmith@gmail.com'))

    def test_pastes1(self):
        self.assertIsNone(self.pwned.pastes('johnsmith007@gmail.com'))
