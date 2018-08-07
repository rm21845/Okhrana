import requests


class hunter(object):
    def __init__(self, key):
        self.key = '&api_key=' + str(key)
        self.base = 'https://api.hunter.io/v2/'

    def domain(self, domain):
        """Get every email address found on the internet using a given domain name or comp, with sources."""
        r = requests.get(self.base + 'domain-search?domain=' + str(domain) + self.key).json()

        return [email['value'] for email in r['data']['emails']]

    def name(self, domain, first, last):
        """Find the email address of someone from his first name, last name and domain name."""
        r = requests.get(self.base + 'email-finder?domain=' + str(domain) +
                            '&first_name=' + str(first) + '&last_name=' + str(last) + self.key).json()

        data = r['data']
        return [data['first_name'], data['last_name'], data['email'], data['domain'], data['position']]

    def verify_email(self, email):
        """Check if a given email address is deliverable and has been found on the internet."""
        r = requests.get(self.base + 'email-verifier?email=' + str(email) + self.key).json()

