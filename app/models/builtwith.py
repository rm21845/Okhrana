import requests

class builtwith():
    def __init__(self, key):
        self.base = 'https://api.builtwith.com/free1/api.json'
        self.key = '?KEY=' + str(key)

    def domain(self, domain):
        r = requests.get(self.base + self.key + '&LOOKUP=' + str(domain))
        if r.status_code == 200:
            return requests.get(self.base + self.key + '&LOOKUP=' + str(domain)).json()