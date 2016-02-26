#!/usr/bin/env python
__author__ = 'victor'

import sys



def read_mapper_output(file, separator='\t\t'):
    for line in file:
        yield line.split(separator, 1) #Genero estructura Key \t\t Value


def main(separator='\t\t'):
    auxip = ""
    auxmac = ""
    data = read_mapper_output(sys.stdin, separator=separator)

    for datos, valor in data:
        ip, hora, mac = datos.split(';')
        if str(ip) != auxip or str(mac) != auxmac:
            print(ip + '\t' + hora + '\t' + mac)
            auxip, auxmac = ip, mac

if __name__ == "__main__":
    main()
