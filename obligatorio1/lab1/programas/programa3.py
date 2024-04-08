# -*- coding: utf-8 -*-
import re
import sys

def prog(texto):
    #patron_timestamp = r'(\d{4})-(\d{2})-(\d{2}) (\d{2}):(\d{2}):(\d{2})'
    meses = {'01': 'enero', '02': 'febrero', '03': 'marzo', '04': 'abril', '05': 'mayo', '06': 'junio', 
             '07': 'julio', '08': 'agosto', '09': 'septiembre', '10': 'octubre', '11': 'noviembre', '12': 'diciembre'}

    match = re.findall(r'"timestamp": "T (.*):\d{2}",', texto)
    aux = list()
    fechas = ""
    fechas = [re.sub(r'(\d{4}):(\d{2}):(\d{2}) (\d{2}):(\d{2}).*', 
                     lambda m: f"{m.group(3)} de {meses[m.group(2)]} del {m.group(1)} a las {m.group(4)}:{m.group(5)} hs.", 
                     fecha) for fecha in match]
    return '\n'.join(fechas)


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
