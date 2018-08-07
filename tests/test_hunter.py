import unittest
from app.models.hunter import hunter


class HunterTestCase(unittest.TestCase):
    def setUp(self):
        self.hunter = hunter('42550a5b12fc272f631b6e2354858257741d73c3')

    def test_domain(self):
        self.assertIsNotNone(self.hunter.domain('github.com'))

    def test_name(self):
        self.assertIsNone(print(self.hunter.name('github.com', 'john', 'smith')))

    def test_verify(self):
        self.assertIsNone(print(self.hunter.verify_email('ace@gmail.com')))
