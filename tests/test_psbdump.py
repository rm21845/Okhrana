import unittest
from app.models.psbdmp import psbdmp


class PsbdumpTestCase(unittest.TestCase):
    def setUp(self):
        self.psbdmp = psbdmp()

    def test_search0(self):
        self.assertIsNotNone(self.psbdmp.search('johnsmith'))

    def test_search1(self):
        self.assertIsNotNone(self.psbdmp.search('fuckyou'))

    def test_search2(self):
        self.assertIsNotNone(self.psbdmp.search('bannon'))

    def test_domain0(self):
        self.assertIsNotNone(self.psbdmp.domain('facebook.com'))

    def test_domain1(self):
        self.assertIsNotNone(self.psbdmp.domain('fefefrefv.com'))

    def test_domain2(self):
        self.assertIsNotNone(self.psbdmp.domain('factual.com'))

    def test_email0(self):
        self.assertIsNotNone(self.psbdmp.email('johnsmith32434@gmail.com'))

    def test_email1(self):
        self.assertIsNotNone(self.psbdmp.email('johnsmith@gmail.com'))

    def test_email2(self):
        self.assertIsNotNone(self.psbdmp.email('facebook@gmail.com'))

