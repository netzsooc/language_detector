'''
Created on 16/10/2012

@author: netzsooc
'''
import urllib2
tdb = {}
def parse_file(fname):
    print "Recuperando archivo, puede tardar..."
    arch = urllib2.Request(fname)
    arch.add_header('User-agent', 'Mozilla/5.0')
    arch = urllib2.urlopen(arch)
    par = '  '
    for line in arch:
        for char in line.rstrip().strip():
            print 'par es =', par
            d = tdb.setdefault(par, {})
            d[char] = d.get(char, 0) + 1
            par = par[1] + char
            print 'par es =', par
    print measure()
    
def measure():
    print 'aqui'
    total = 0
    
    for y in tdb.values():
        total += sum([x * x for x in y.values()])
        
    length = total ** 0.5