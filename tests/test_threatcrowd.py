import unittest
from app.models.threatcrowd import threat_crowd


class threatCrowdTestCase(unittest.TestCase):
    def setUp(self):
        self.tc = threat_crowd()

    def test_domain1(self):
        self.assertIsNone(self.tc.domain('ebay.com'))

    def test_ipaddr0(self):
        self.assertIsNotNone(self.tc.ip_addr('8.8.8.8'))

    def test_ipaddr1(self):
        self.assertIsNotNone(self.tc.ip_addr('151.101.129.140'))

    def test_ipaddr2(self):
        self.assertIsNotNone(self.tc.ip_addr('172.217.12.206'))

    def test_email0(self):
        self.assertIsNotNone(self.tc.email('johnsmith@gmail.com'))

    def test_email1(self):
        self.assertIsNotNone(self.tc.email('ace@gmail.com'))

    def test_email2(self):
        self.assertIsNotNone(self.tc.email('aristotle@yahoo.com'))
        