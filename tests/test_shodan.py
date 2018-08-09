import unittest
from app.models.shodan import Shodan


class ShodanTestCase(unittest.TestCase):
    def setUp(self):
        self.shodan = Shodan('MdCvBclu3iJqduR78CcshNmrXlTD5DyV')

    def test_ip0(self):
        self.assertIsNotNone(self.shodan.ip_search('172.217.10.46'))

    def test_ip1(self):
        self.assertIsNotNone(self.shodan.ip_search('0.0.0.0'))

    def test_ip2(self):
        self.assertIsNotNone(self.shodan.ip_search('192.30.253.113'))