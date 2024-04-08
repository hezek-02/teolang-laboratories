# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'"user": "(.*)",', texto)
    aux = list()
    contadores = {}
    for usuario in match:
        if usuario not in aux:
            aux.append(usuario)
            contadores[usuario] = 1
        else:
            contadores[usuario] = contadores[usuario] + 1
    
    ret = "\n".join([f"{usuario}: {contadores[usuario]}" for usuario in contadores])
    return ret

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
