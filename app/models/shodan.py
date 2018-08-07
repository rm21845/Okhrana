import requests


class Shodan(object):
    def __init__(self, api):
        self.base = 'https://api.shodan.io'
        self.api = '?key=' + str(api)

    def ip_search(self, ip_addr):
        r = requests.get(self.base + '/shodan/host/' + str(ip_addr) + str(self.api)).json()
        print('region_code')
        print(r['region_code'])
        print('ip')
        print(r['ip'])
        print('country_name')
        print(r['country_name'])
        print('postal_code')
        print(r['postal_code'])
        print('data')
        print(len(r['data']))
