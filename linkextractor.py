#!/usr/bin/python
"""
Finds all links on a html page with regular expression.
"""

import re
import urllib2

matches = []
url = "http://www.nyt.com"
pattern = re.compile("href= *\"([^\"]+)")

try:
    response = urllib2.urlopen(url)
    html = response.read()
    response.close()
except:
    print "Something, somewhere went terribly wrong."
else:
    matches = re.findall(pattern, html)
    for link in matches:
        print link
