import unittest
from app.models.hunter import hunter


class HunterTestCase(unittest.TestCase):
    def setUp(self):
        self.hunter = hunter('42550a5b12fc272f631b6e2354858257741d73c3')

    def test_domain0(self):
        self.assertIsNotNone(self.hunter.domain('github.com'))

    def test_domain1(self):
        self.assertIsNotNone(self.hunter.domain('weleakinfo.com'))

    def test_domain2(self):
        self.assertIsNotNone(self.hunter.domain('facebook.com'))

    def test_name0(self):
        self.assertIsNotNone(self.hunter.name('github.com', 'john', 'smith'))

    def test_name1(self):
        self.assertIsNotNone(self.hunter.name('myspace.com', 'sarah', 'walsh'))

    def test_name2(self):
        self.assertIsNotNone(self.hunter.name('adobe', 'steve', 'smith'))

    def test_verify0(self):
        self.assertIsNotNone(self.hunter.verify_email('ace@gmail.com'))

    def test_verify1(self):
        self.assertIsNotNone(self.hunter.verify_email('jarvis@protonmail.com'))

    def test_verify2(self):
        self.assertIsNotNone(self.hunter.verify_email('mike@protonmail.com'))