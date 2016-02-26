#!/usr/bin/env python
__author__ = 'victor'

import sys
import os

def read_mapper_output(file, separator='\t\t'):
    for line in file:
        yield line.rstrip().split(separator, 2) #Genero estructura Fecha \t\t Origin \t\t Count


def main(separator='\t\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    diforigin = set()
    difdate = set()
    result = {}
    output = ""
    cabecera = ""
    sum = 0

    #Genero mi diccionario e inicializo las variables para recorrerlo ordenadamente
    #porque un diccionario no se puede ordenar, solo obtener representaciones ordenadas
    for accessdate, origin, count in data:
        try:
            result.setdefault(accessdate, {})[origin] += int(count)
        except:
            result.setdefault(accessdate, {})[origin] = int(count)
            difdate.add(accessdate)
            diforigin.add(origin)

    for x in sorted(diforigin):
        cabecera += str(x) + ';'

    #Imprimo mi diccionario en el orden y formato elegido
    print("Month;Day;Hour;" + cabecera + "Total")
    for x in sorted(difdate):
        for y in sorted(diforigin):
            try:
                output += str(result[x][y]) + ';'
                sum += result[x][y]
            except:
                output += str(0) + ';'
        print(str(x) + ';' + str(output) + str(sum))
        output = ""
        sum = 0

    #sys.stderr.write("reporter:counter:Temperature,Missing,1\n")


if __name__ == "__main__":
    main()