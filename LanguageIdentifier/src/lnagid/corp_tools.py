'''
Created on Oct 26, 2012

@author: netzsooc
'''
from urls import open_as_mozilla

def corpus_compiler(lista):
    out = ''
    for fn in lista:
        print "abriendo %s" % (fn[fn.rfind("/") + 1:])
        arch = open_as_mozilla(fn)
        out += arch.read()
    return out


#esfiles = ['http://www.gutenberg.org/cache/epub/33885/pg33885.txt', 
#           'http://www.gutenberg.org/cache/epub/26508/pg26508.txt', 
#           'http://www.gutenberg.org/cache/epub/26231/pg26231.txt']
#
#
#defiles = ['http://www.gutenberg.org/files/14225/14225-0.txt', 
#           'http://www.gutenberg.org/files/16880/16880-0.txt',
#           'http://www.gutenberg.org/cache/epub/39669/pg39669.txt']
#
#enfiles = ['http://www.gutenberg.org/dirs/etext05/cfgsh10.txt',
#           'http://www.gutenberg.org/cache/epub/76/pg76.txt', 
#           'http://www.gutenberg.org/cache/epub/1661/pg1661.txt']