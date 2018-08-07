import requests


class Social(object):
    def by_username(self, username):
        reddit = requests.get('https://www.reddit.com/user/' + str(username)).status_code == 200
        tumblr = requests.get('http://' + str(username) + '.tumblr.com/').status_code == 200
        instagram = requests.get('https://www.instagram.com/' + str(username)).status_code == 200
        pinterest = requests.get('https://www.pinterest.com/' + str(username)).status_code == 200
        vkdotcom = requests.get('https://vk.com/' + str(username)).status_code == 200
        linkedin = requests.get('https://www.linkedin.com/in/' + str(username)).status_code == 200
        taringa = requests.get('https://www.taringa.net/' + str(username)).status_code == 200
        foursquare = requests.get('https://foursquare.com/' + str(username)).status_code == 200
        myspace = requests.get('https://myspace.com/' + str(username)).status_code == 200
        facebook = requests.get('https://facebook.com/' + str(username)).status_code == 200
        smule = requests.get('https://www.smule.com/' + str(username)).status_code == 200

    def snapchat(self, username):
        ghostcode = requests.get('https://www.ghostcodes.com/' + str(username)).status_code == 200
        snapvip = requests.get('https://snapvip.io/' + str(username)).status_code == 200