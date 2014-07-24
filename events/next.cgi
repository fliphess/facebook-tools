#!/usr/bin/env python
import cgi
import cgitb
import urllib2
import json

from html.page import header, table, footer
from django.utils.encoding import smart_str

cgitb.enable()

access_token = "YOURACCESSTOKEN"
form = cgi.FieldStorage()
event_id = form.getvalue('event')

print 'Content-type: text/html\r\n\r'

if not event_id:
    print "Failed"
else:
    try:
        event = urllib2.urlopen("https://graph.facebook.com/%s/attending?access_token=%s"%(event_id, access_token))
    except Exception:
        event = False

    if event:
        raw_data = event.read()
        attendees = json.loads(raw_data)
        names = [ a['name'] for a in attendees['data']]

        print header % (event_id, len(attendees['data']))
        for name in sorted(names):
            print table % smart_str(name.encode('ascii', 'xmlcharrefreplace'))
        print footer 
    else: 
        print "Failed"

