import requests


class Shodan(object):
    def __init__(self, api):
        self.base = 'https://api.shodan.io'
        self.api = '?key=' + str(api)

    def ip_search(self, ip_addr):
        r = requests.get(self.base + '/shodan/host/' + str(ip_addr) + str(self.api)).json()
        results = dict()
        try:
            results['region_code'] = r['region_code']
        except KeyError:
            pass 
        try:
            results['ip_addr'] = r['ip']
        except KeyError:
            pass
        try:
            results['country'] = r['country_name']
        except KeyError:
            pass
        try:
            results['postal'] = r['postal_code']
        except KeyError:
            pass

        return results
