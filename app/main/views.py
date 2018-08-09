from flask import render_template, session, redirect, url_for, request
from app.models.hibp import hibp
from app.models.psbdmp import psbdmp
from app.models.hunter import hunter
from app.models.threatcrowd import threat_crowd
from app.models.social import Social
from app.models.twitter_srch import twitter
from app.models.builtwith import builtwith 
from app.models import github
from app.helpers import validation
from app.helpers.parser import parsing
from . import main
#from .. import db
from . import forms

@main.route('/', methods=['GET', 'POST'])
def index():
    form = forms.ScanForm()

    return render_template('views/index.html', form=form)


@main.route('/scan', methods=['GET', 'POST'])
def scan():
    data = request.form['search']
    results = dict()
    haveibeen = hibp()
    pastedump = psbdmp()
    hunt = hunter('42550a5b12fc272f631b6e2354858257741d73c3')
    tc = threat_crowd()
    social = Social()
    pr = parsing()
    #twitter = twitter_srch('')
    bw = builtwith('aeef2291-5ce8-4408-886d-f38989fb6d37')

    scan_type = request.form['scan']
    print(scan_type)

    if(scan_type == 'passive'):
        if validation.email_validation(data):
            results['hibn_breaches'] = haveibeen.breaches(data)
            results['hibn_pastes'] = haveibeen.pastes(data)
            results['psbdmp.pw'] = pastedump.email(data)
            results['hunter emails'] = hunt.verify_email(data)
            results['Threat Crowd'] = tc.email(data)

            #parse to use username
            username = pr.parse_email(data)
            results['hibn_breaches as user'] = haveibeen.breaches(username)
            results['psbdmp.pw as user'] = pastedump.search(username)
            results['Social Accounts'] = social.by_username(username)
            results['Github as user'] = github.user(username)
            #results['Twitter as user'] = twitter.search_user(data)


        elif validation.domain_validation(data):
            results['psbdmp.pw'] = pastedump.domain(data)
            results['hunter emails'] = hunt.domain(data)
            results['Threat Crowd'] = tc.domain(data)
            results['Built With'] = bw.domain(data)

            #parse to use as username or company
            username = pr.parse_dom(data)
            results['hibn_breaches as user'] = haveibeen.breaches(username)
            results['psbdmp.pw as user'] = pastedump.search(username)
            results['Social Accounts'] = social.by_username(username)
            results['Github as user'] = github.org(username)
            #results['Twitter as user'] = twitter.search_user(data)

        elif validation.ip_validation(data):
            print('Data is ip')
            results['Threat Crowd'] = tc.ip_addr(data)
        else:
            results['hibn_breaches'] = haveibeen.breaches(data)
            results['psbdmp.pw'] = pastedump.search(data)
            results['Social Accounts'] = social.by_username(data)
            results['Github'] = github.user(data)
            #results['Twitter'] = twitter.search_user(data)


    return render_template('views/scan.html', data=data, results=results)