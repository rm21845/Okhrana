import requests


class psbdmp(object):
    def __init__(self):
        self.base = 'https://psbdmp.ws/api/search/'

    def search(self, data):
        r = requests.get(self.base + str(data)).json()
        return ['https://pastebin.com/' + str(paste['id']) for paste in r['data']]

    def domain(self, domain):
        r = requests.get(self.base + 'domain/' + str(domain)).json()
        return ['https://pastebin.com/' + str(paste['id']) for paste in r['data']]

    def email(self, email):
        """Getting dump(s) by email."""
        r = requests.get(self.base + 'email/' + str(email)).json()
        return ['https://pastebin.com/' + str(paste['id']) for paste in r['data']]

