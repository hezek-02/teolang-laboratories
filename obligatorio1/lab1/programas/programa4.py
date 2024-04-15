# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    match = re.findall(r'#+(.*?)\\n', texto) #necesito seleccionar el texto entre el(los) # y el salto de línea
    ret = '\n'.join(match)

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


#5.5 programa4.py
#Despliega los encabezados (de cualquier tipo) de los mensajes, en orden de
#aparición en el json (se devuelve solo el texto, sin los #).
#Con el archivo de ejemplo (0.json) se obtiene la siguiente salida:
#Python
#Muchas gracias