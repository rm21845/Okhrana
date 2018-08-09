import requests

class threat_crowd(object):
    """The ThreatCrowd API allows you to quickly identify related infrastructure and malware."""
    def __init__(self):
        self.base = 'https://www.threatcrowd.org/searchApi/v2/'

    def domain(self, domain):
        try: 
            return requests.get(self.base + 'domain/report/?domain=' + str(domain)).json()
        except:
            pass  
        
    def ip_addr(self, ip_addr):
        try:
            return requests.get(self.base + 'ip/report/?ip=' + str(ip_addr)).json()
        except:
            pass 

    def email(self, email):
        try:
            return requests.get(self.base + 'email/report/?email=' + str(email)).json()
        except:
            pass 

