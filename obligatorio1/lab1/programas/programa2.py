# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'"user": "(.*?)",', texto)
    aux = list()
    for usuario in list(dict.fromkeys(match)): #se eliminan duplicados dict from keys toma un representante de cada elemento y luego lo convierte en lista
            apariciones = len(re.findall(f'"user": "{usuario}",', texto))
            aux.append(f"{usuario}: {apariciones}")
    return '\n'.join(aux)

if __name__ == '__main__':
    entrada = sys.argv[1]  # archivo entrada (param)
    salida = sys.argv[2]   # archivo salida (param)
    
    f = open(entrada, 'r') # abrir archivo entrada
    datos = f.read()       # leer archivo entrada
    f.close()              # cerrar archivo entrada
    
    ret = prog(datos)      # ejecutar er
    
    f = open(salida, 'w')  # abrir archivo salida
    f.write(ret)           # escribir archivo salida
    f.close()              # cerrar archivo salida
