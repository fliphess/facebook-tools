#!/usr/bin/env python
import cgi
import cgitb
from html.page import form
cgitb.enable()

print 'Content-type: text/html\r\n\r'
print form
