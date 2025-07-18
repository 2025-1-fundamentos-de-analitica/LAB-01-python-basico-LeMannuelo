"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    archivo = "files/input/data.csv"
    conteo_claves = {}

    with open(archivo, newline='', encoding='utf-8') as f:
        lector = csv.reader(f, delimiter='\t')
        for fila in lector:
            pares = fila[4].split(',')
            for par in pares:
                clave, _ = par.split(':')
                conteo_claves[clave] = conteo_claves.get(clave, 0) + 1

    return dict(sorted(conteo_claves.items()))
