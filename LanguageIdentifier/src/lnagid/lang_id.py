#-*- encoding: UTF-8 -*-
'''
Created on 16/10/2012

@author: netzsooc
'''
from random import choice
import urllib2

class trig(object):
    '''
    '''
    
    length = 0


    def __init__(self, fname = None, flag = True):
        '''
        Constructor
        '''
        self.tdb = {}
        if fname:
            if flag:
                self.parse_file(fname)
            else:
                self.parse_cadena(fname)
            
    
    def parse_file(self, fname):
                
        if '://' in fname:
            print "Recuperando archivo, puede tardar..."
            arch = self.open_as_mozilla(fname)
        else:
            arch = open(fname)
            
        for linea in arch:
            self.parse_una_cadena(linea)

        arch.close()
        self.measure()
        
    
    def open_as_mozilla(self,url):
        arch = urllib2.Request(url)
        arch.add_header('User-agent', 'Mozilla/5.0')
        return urllib2.urlopen(url)
    
    
    def parse_cadena(self, cadena, par = '  '):
        self.parse_una_cadena(cadena, par)
        self.measure()    
        
        
    def parse_una_cadena(self, cadena, par = '  '):
        
        for char in cadena.rstrip().strip():
                vector = self.tdb.setdefault(par, {})
                vector[char] = vector.get(char, 0) + 1
                par = par[1] + char

        
    def measure(self):
        total = 0
        
        for y in self.tdb.values():
            total += sum([x * x for x in y.values()])
            
        self.length = total ** 0.5
        
        
    def similaridad(self, otro):
        if not isinstance(otro, trig):
            raise TypeError("No es posible comparar un trig con un no trig")
        tdb1 = self.tdb
        tdb2 = otro.tdb
        total = 0
        
        for k in tdb1.keys():
            if k in tdb2:
                a = tdb1[k]
                b = tdb2[k]
                
                for x in a:
                    if x in b:
                        total+= a[x] * b[x]
                        
        return float(total) / (self.length * otro.length)
    
       
    def inventa_palabras(self, cuenta):
        texto = []
        k = '  '
        while cuenta:
            n = self.probable(k)
            texto.append(n)
            k = k[1] + n
            if n in ' \t':
                cuenta -= 1
        return ''.join(texto)
    
    
    def probable(self, k):
        if k not in self.tdb:
            return ' '
        
        letras = []
        
        for k, v in self.tdb[k].items():
            letras.append(k * v)
            
        letras = "".join(letras)
        return choice(letras)
    
    
def corpus_compiler(lista):
    out = ''
    for fn in lista:
        print "abriendo %s" % (fn[fn.rfind("/") + 1:])
        arch = urllib2.Request(fn)
        arch.add_header('User-agent', 'Mozilla/5.0')
        arch = urllib2.urlopen(arch)
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
#
#with open('falso_es', 'w') as f:
#    f.write(corpus_compiler(esfiles))
#    
#with open('falso_en', 'w') as f:
#    f.write(corpus_compiler(enfiles))
#    
#with open('falso_de', 'w') as f:
#    f.write(corpus_compiler(defiles))
    
es = trig('falso_es')
en = trig('falso_en')
de = trig('falso_de')

desc = 'hola'
unk = trig(desc, 0)
sel = {es.similarity(unk): "es", en.similarity(unk): 'en', 
       de.similarity(unk): 'de'} 
lang = sel[max(sel)]
print sel
print "phrase: %s \nlanguage: %s" % (desc, lang)

print es.inventa_palabras(100)