'''
Created on Oct 25, 2012

@author: netzsooc
'''
import urllib2


def open_as_mozilla(url):
    arch = urllib2.Request(url)
    arch.add_header('User-agent', 'Mozilla/5.0')
    return urllib2.urlopen(url)