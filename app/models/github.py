import requests


class github():
    def user(self, username):
        r = requests.get('https://api.github.com/users/' + str(username)).json()
        results = dict()

        results['login'] = r['login']
        results['url'] = r['url']
        results['name'] = r['name']
        results['company'] = r['company']
        results['location'] = r['location']
        results['email'] = r['email']
        results['bio'] = r['bio']

        return results

    def org(selfself, name):
        r = requests.get('https://api.github.com/orgs/' + str(name)).json()
        results = dict()

        results['login'] = r['login']
        results['url'] = r['url']
        results['name'] = r['name']
        results['company'] = r['company']
        results['location'] = r['location']
        results['email'] = r['email']
        results['billing'] = r['billing_email']

        return results