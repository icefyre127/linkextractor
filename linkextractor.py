#!/usr/bin/python

import urllib2
import re
pattern = re.compile("href= *\"([^\"]+)")


#with open("test.html") as textfile:
#    text = textfile.read()

text = urllib2.urlopen("http://www.nyt.com").read()

matches = re.findall(pattern,text)

for link in matches:
    print link
