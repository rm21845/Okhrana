import unittest
from app.models.psbdmp import psbdmp


class PsbdumpTestCase(unittest.TestCase):
    def setUp(self):
        self.psbdmp = psbdmp()

    def test_search(self):
        self.assertIsNotNone(self.psbdmp.search('johnsmith'))

    def test_domain(self):
        self.assertIsNotNone(self.psbdmp.domain('weleakinfo.com'))

    def test_email(self):
        self.assertIsNotNone(self.psbdmp.email('johnsmith@gmail.com'))