import requests

def user(username):
    r = requests.get('https://api.github.com/users/' + str(username)).json()
    results = dict()
    try:
        results['login'] = r['login']
    except KeyError:
            pass
    try:
        results['url'] = r['url']
    except KeyError:
            pass 
    try:
        results['name'] = r['name']
    except KeyError:
            pass
    try:
        results['company'] = r['company']
    except KeyError:
            pass
    try:
        results['location'] = r['location']
    except KeyError:
            pass
    try:
        results['email'] = r['email']
    except KeyError:
            pass
    try:
        results['bio'] = r['bio']
    except KeyError:
            pass
    return results

def org(name):
    r = requests.get('https://api.github.com/orgs/' + str(name)).json()
    results = dict()

    try:
        results['login'] = r['login']
    except KeyError:
            pass
    try:
        results['url'] = r['url']
    except KeyError:
            pass 
    try:
        results['name'] = r['name']
    except KeyError:
            pass 
    try:
        results['company'] = r['company']
    except KeyError:
            pass 
    try:
        results['location'] = r['location']
    except KeyError:
            pass 
    try:
        results['email'] = r['email']
    except KeyError:
            pass 
    return results