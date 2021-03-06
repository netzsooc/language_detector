#-*- encoding: UTF-8 -*-
'''
Created on 16/10/2012

@author: netzsooc
'''
from random import choice
from urls import open_as_mozilla


class trig(object):
    '''
    '''
    
    length = 0


    def __init__(self, fname = None, t_file = True):
        '''
        Constructor
        '''
        self.tdb = {}
        if fname:
            if t_file:
                self.parse_file(fname)
            else:
                self.parse_cadena(fname)
            
    
    def parse_file(self, fname):
                
        if '://' in fname:
            print "Recuperando archivo, puede tardar..."
            arch = open_as_mozilla(fname)
        else:
            arch = open(fname)
            
        for linea in arch:
            self.parse_una_cadena(linea)

        arch.close()
        self.measure()
    
    
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

    



def main():
    es = trig('falso_es')
    en = trig('falso_en')
    de = trig('falso_de')
    
    desc = ' '
    while desc:
        desc = raw_input("write down your term please:\n")
        unk = trig(desc, 0)
        sel = {es.similaridad(unk): "es", en.similaridad(unk): 'en', 
               de.similaridad(unk): 'de'} 
        lang = sel[max(sel)]
        print "phrase: %s \nlanguage: %s" % (desc, lang)
        
    print "Gracias."


if __name__ == "__main__":
    main()