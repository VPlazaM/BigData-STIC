#!/usr/bin/env python
__author__ = 'victor'

import sys

def read_mapper_output(file, separator='\t\t'):
    for line in file:
        yield line.rstrip().split(separator, 2) #Genero estructura IP \t\t Path \t\t Count


def main(separator='\t\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    diffiles = set()
    difip = set()
    result = {}
    output = ""
    cabecera = ""
    sum = 0

    #Genero mi diccionario e inicializo las variables para recorrerlo ordenadamente
    #porque un diccionario no se puede ordenar, solo obtener representaciones ordenadas
    for ip, path, count in data:
        try:
            result.setdefault(ip, {})[path] += int(count)
            difip.add(ip)
            diffiles.add(path)
        except:
            result.setdefault(ip, {})[path] = 1
            difip.add(ip)
            diffiles.add(path)

    for x in sorted(diffiles):
        cabecera += x + '\t'

    #Imprimo mi diccionario en el orden y formato elegido
    print("Month\tDay\tHour\tIp\t", cabecera, "Total")
    for x in sorted(difip):
        for y in sorted(diffiles):
            try:
                output += str(result[x][y]) + '\t'
                sum += result[x][y]
            except:
                output += str(0) + '\t'
        print(x, '\t', output, sum)
        output = ""
        sum = 0



if __name__ == "__main__":
    main()