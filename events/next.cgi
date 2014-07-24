#!/usr/bin/env python
import cgi
import cgitb
from types import NoneType
import urllib2, json, re, sys
from html.page import header, table, footer
from django.utils.encoding import smart_str, smart_unicode

cgitb.enable()

access_token = "YOURACCESSTOKEN"
form = cgi.FieldStorage()
event_id = form.getvalue('event')

print 'Content-type: text/html\r\n\r'

if event_id:
    try:
        event = urllib2.urlopen("https://graph.facebook.com/%s/attending?access_token=%s"%(event_id, access_token))
    except Exception:
        event = False

    if event:
        attendees_list = event.read()
        attendees_json = json.loads(attendees_list)
        print header % (event_id, len(attendees_json['data']))
        names = [ a['name'] for a in attendees_json['data']]
        for name in sorted(names):
            print table % smart_str(name.encode('ascii', 'xmlcharrefreplace'))
        print footer 
    else: 
        print "Failed"

else:
    print "Failed"

