import requests


class Shodan(object):
    def __init__(self, api):
        self.base = 'https://api.shodan.io'
        self.api = '?key=' + str(api)

    def ip_search(self, ip_addr):
        r = requests.get(self.base + '/shodan/host/' + str(ip_addr) + str(self.api)).json()
        results = dict()
        results['region_code'] = r['region_code']
        results['ip_addr'] = r['ip']
        results['country'] = r['country_name']
        results['postal'] = r['postal_code']


"""
        for key in r['data']:
            print(key)
"""
