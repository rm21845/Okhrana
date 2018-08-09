import requests


class Social(object):
    def by_username(self, username):
        results = []

        if requests.get('https://www.reddit.com/user/' + str(username)).status_code == 200:
            results.append('https://www.reddit.com/user/' + str(username))

        if requests.get('http://' + str(username) + '.tumblr.com/').status_code == 200:
            results.append('http://' + str(username) + '.tumblr.com/')

        if requests.get('https://www.instagram.com/' + str(username)).status_code == 200:
            results.append('https://www.instagram.com/' + str(username))

        if requests.get('https://www.pinterest.com/' + str(username)).status_code == 200:
            results.append('https://www.pinterest.com/' + str(username))

        if requests.get('https://vk.com/' + str(username)).status_code == 200:
            results.append('https://vk.com/' + str(username))

        if requests.get('https://www.linkedin.com/in/' + str(username)).status_code == 200:
            results.append('https://www.linkedin.com/in/' + str(username))

        if requests.get('https://www.taringa.net/' + str(username)).status_code == 200:
            results.append('https://www.taringa.net/' + str(username))

        if requests.get('https://myspace.com/' + str(username)).status_code == 200:
            results.append('https://myspace.com/' + str(username))

        if requests.get('https://facebook.com/' + str(username)).status_code == 200:
            results.append('https://facebook.com/' + str(username))

        if requests.get('https://www.smule.com/' + str(username)).status_code == 200:
            results.append('https://www.smule.com/' + str(username))

        return results

"""
  def snapchat(self, username):
        if requests.get('https://www.ghostcodes.com/' + str(username)).status_code == 200:
            return 'https://www.ghostcodes.com/' + str(username)

        if requests.get('https://snapvip.io/' + str(username)).status_code == 200:
            return 'https://snapvip.io/' + str(username)
        return ""
"""