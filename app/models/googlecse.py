 import requests

class googlecse(object):
    def __init__(self, key):
        self.base = 'https://www.googleapis.com/customsearch/v1/'
        self.key = '#AIzaSyB-FwHME13Ss5LWTMmJ5Dq6PJo9ZRpRAAU'


    def email(self, email):
        print('Google email search')


    def domain(self, domain):
        """Discover subdomains and sensitive info
            using dorks(i.e inurl:, site:) via seclists
        """