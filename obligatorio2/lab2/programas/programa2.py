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
    '''if tree:
        for i, tree in enumerate(tree):#dibujitos de arbolitos
            print(f"Arbolinho {i+1}:")
            tree.draw()
    else:
        print("NO TA")
    '''
    return tree

#formatea cadenas donde le otorga precedencia a los operadores * y /. si la cadena original es 3 + 4 * 2 -> 3 + (4 * 2), se deben respetar los espacios de las entradas 
#probar mas, idea encontrar operadores * y / y añadir parentesis a los numeros que estan a su alrededor

def formateo_prec(s):
    s = "  " + s + "  "
    ocurrencias = 0
    if "*" in s or "/" in s:
        largo = len(s)
        i = 0
        while i < largo:
            if s[i] == "*" or s[i] == "/": # si tiene * o /
                print(i)
                #LADO IZQUIERDO
                j = i-1
                while s[j] == ' ' or s[j] == ')' or s[j] == '(': # iterar hasta hallar num
                    j -= 1
                    if s[j] == ')': #tener en cuenta parentesis de cierre
                        ocurrencias+=1
                    elif s[j] == '(' and ocurrencias > 0:
                        ocurrencias-=1

                while s[j] != ' ':#se hallo num, iterar hasta espacio vacio
                    j -= 1
                    if s[j] == ')': #tener en cuenta parentesis de cierre
                        ocurrencias+=1
                    elif  s[j] == '(' and ocurrencias > 0:
                        ocurrencias-=1
                
                while  ocurrencias > 0 and j > 0: # espacio vacio pero aun parentesis sin cerrar
                    j -= 1
                    if s[j] == '(':
                        ocurrencias -= 1
                    elif s[j] == ')':
                        ocurrencias += 1
                
                #LADO DERECHO
                if ocurrencias == 0:
                    k = i+1
                    
                    while s[k] == ' ' or s[k] == ')' or s[k] == '(':# iterar hasta hallar num, lado derecho
                        k += 1
                        if s[k] == '(': # tener en cuenta parentesis
                            ocurrencias+=1
                        elif s[k] == ')' and ocurrencias > 0:
                            ocurrencias-=1    


                    while s[k] != ' ':#iterar hasta espacio vacio
                        k += 1
                        if s[k] == '(':#tener en cuenta parentesis, no tiene mucho sentido aqui
                            ocurrencias += 1
                        elif  s[k] == ')' and ocurrencias > 0:
                            ocurrencias-=1
                    k += 1

                    while ocurrencias > 0 and k < largo:# espacio vacio pero aun parentesis sin cerrar
                        k += 1
                        if s[k] == '(':
                            ocurrencias += 1
                        elif s[k] == ')':
                            ocurrencias -= 1

                    #print(s[j:k])
                    if ocurrencias == 0:
                        s = s[:j] + "(" + s[j:k]  + ")" + s[k:]
            else:
                i += 2
    return s
# de S O S a O(S,S), de N a N,no cuenta precedencia
#3+4*2 -> +(*(4,2),3)
#3 + 4 * 2 -> *(+(3,4),2)
def transformation(tree):
    palabra = ""
    S_rigth = False
    S_left = False
    O = False
    izq = ""
    der = ""
    for i in tree:

        '''if type(i) is nltk.Tree:
            print(i.label())
        else:
            print(i)'''
        
        if type(i) is nltk.Tree and i.label() == 'S':
            if S_left:
                S_rigth = i
            else: 
                S_left = i
                palabra = transformation(S_left)
            if S_left and S_rigth:
                izq = palabra
                der = transformation(S_rigth)
                palabra = O + "(" + izq + "," + der + ")"
        if type(i) is nltk.Tree and i.label() == 'O':
            O = i.leaves()[0]
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
      #añade parentesis a las operaciones de mayor precedencia * y /
      s = formateo_prec(s)
      #print(s)
      tree = parse(s, grammar)
      if tree:
        palabra = transformation(tree)
        #print("palabra: " + palabra)
        salida = palabra
      else:
        salida = "NO PERTENECE"
    except ValueError:
      salida = "NO PERTENECE - FUERA DE ALFABETO"
    f = io.open(archivo_salida, 'w', newline='\n', encoding='utf-8')
    f.write(salida)
    f.close()
