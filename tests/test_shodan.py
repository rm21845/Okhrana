import unittest
from app.models.shodan import Shodan


class ShodanTestCase(unittest.TestCase):
    def setUp(self):
        self.shodan = Shodan('MdCvBclu3iJqduR78CcshNmrXlTD5DyV')

    def test_ip(self):
        print(self.shodan.ip_search('172.217.10.46'))