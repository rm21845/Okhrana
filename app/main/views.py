from flask import render_template, session, redirect, url_for, request
from app.models.hibp import hibp
from app.models.psbdmp import psbdmp
from app.models.hunter import hunter

from . import main
#from .. import db
from . import forms
import re

def email_validation(data):
    match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', data)
    return match != None

def domain_validation(data):
    match = re.match('(([\da-zA-Z])([_\w-]{,62})\.){,127}(([\da-zA-Z])[_\w-]{,61})?([\da-zA-Z]\.((xn\-\-[a-zA-Z\d]+)|([a-zA-Z\d]{2,})))', data)
    return match != None

def ip_validation(data):
    match = re.match('^(?:(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.){3}(?:[0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$', data)
    return match != None

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
    hunt = hunter()

    scan_type = request.form['scan']
    print(scan_type)

    if(scan_type == 'passive'):
        if email_validation(data):
            results['hibn_breaches'] = haveibeen.breaches(data)
            results['hibn_pastes'] = haveibeen.pastes(data)
            results['psbdmp.pw'] = pastedump.email(data)
            results['hunter emails'] = hunt.verify_email(data)

        elif domain_validation(data):
            results['psbdmp.pw'] = pastedump.domain(data)
            results['hunter emails'] = hunt.domain(data)
        elif ip_validation(data):
            print('Data is ip')
        else:
            results['hibn_breaches'] = haveibeen.breaches(data)
            results['psbdmp.pw'] = pastedump.search(data)


    return render_template('views/scan.html', data=data, results=results)