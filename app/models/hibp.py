import requests


class hibp(object):
    def breaches(self, data):
        """
        :param data: username, name, email
        :return: list of breaches assoc. w/ data
        """
        r = requests.get('https://haveibeenpwned.com/api/v2/breachedaccount/' + str(data)).json()
        return [breach['Title'] for breach in r]

    def pastes(self, email):
        """TODO: some decoding errors"""
        r = requests.get('https://haveibeenpwned.com/api/v2/pasteaccount/' + str(email)).json()
        pastes = ['https://pastebin.com/' + str(paste['Id']) for paste in r if paste['Source'] == 'Pastebin']
        pastes += [str(paste['Id']) for paste in r if paste['Source'] == 'AdHocUrl']
        return pastes
