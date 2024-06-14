# -*- coding: utf-8 -*-

import sys
import io
import nltk
import ssl
from nltk.parse.generate import generate
#ssl._create_default_https_context = ssl._create_unverified_context
#nltk.download('punkt')


# grammar definition
grammar = """
S -> N | S O S | '('S')'
N -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9' | '10' | '11' | '12' | '13' | '14' | '15' | '16' | '17' | '18' | '19' | '20' | '21' | '22' | '23' | '24' | '25' | '26' | '27' | '28' | '29' | '30' | '31' | '32' | '33' | '34' | '35' | '36' | '37' | '38' | '39' | '40' | '41' | '42' | '43' | '44' | '45' | '46' | '47' | '48' | '49' | '50' | '51' | '52' | '53' | '54' | '55' | '56' | '57' | '58' | '59' | '60' | '61' | '62' | '63' | '64' | '65' | '66' | '67' | '68' | '69' | '70' | '71' | '72' | '73' | '74' | '75' | '76' | '77' | '78' | '79' | '80' | '81' | '82' | '83' | '84' | '85' | '86' | '87' | '88' | '89' | '90' | '91' | '92' | '93' | '94' | '95' | '96' | '97' | '98' | '99' | '100' 
O -> '+' | '-' | '*' | '/'
"""

#se emplea N -> todos los numeros del 0 a 100, porq por separado no funca
#version anterior que no funciona
#N1 -> '0' | '1'N2 | '2'N2 | '3'N2 | '4'N2 | '5'N2 | '6'N2 | '7'N2 | '8'N2 | '9'N2 | '100' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
#N2 -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'

def parse(s, grammar):
        
    # parser
    grammar = nltk.CFG.fromstring(grammar)
    parser = nltk.LeftCornerChartParser(grammar)
    
    # tokenize
    s_tokenized = nltk.word_tokenize(s)

    # parse
    tree = list(parser.parse(s_tokenized))[:1]
    if tree:
        for i, tree in enumerate(tree):#dibujitos de arbolitos
            #print(f"Arbolinho {i+1}:")
            #tree.draw()
            pass
    else:
        #print("NO TA")
        pass
    return tree


# de S O S a O(S,S), de N a N,no cuenta precedencia
def transformation(tree):
    palabra = ""
    S = False
    O = False
    for i in tree:
        #print(i)
        if type(i) is nltk.Tree and i.label() == 'S':
            if S != False and O != False:
               palabra = O.leaves()[0] + "(" + transformation(S) + "," + transformation(i) + ")"
            else:
                S = i
                palabra = transformation(S)
        elif type(i) is nltk.Tree and i.label() == 'O':
            O = i
        elif type(i) is nltk.Tree and i.label() == 'N':
            palabra = i.leaves()[0]
    return palabra
        

if __name__ == '__main__':
    archivo_entrada = sys.argv[1]
    archivo_salida = sys.argv[2]
    f = io.open(archivo_entrada, 'r', newline='\n', encoding='utf-8')
    s = f.read()
    f.close()
    try:
      tree = parse(s, grammar)
      if tree:
        salida = transformation(tree)
      else:
        salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
