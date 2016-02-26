#!/usr/bin/env python
__author__ = 'victor'

import sys
import zipimport
importer = zipimport.zipimporter('net.mod')
netaddr = importer.load_module('netaddr')
from netaddr.ip import IPAddress, IPNetwork, all_matching_cidrs

def read_input(file):
    for line in file:
        yield line


def main():
    list = []
    global result
    result = {}
    with open("IPS.txt", 'r') as f:
        for line in f:
            if line != "":
                aux = line.split(';')
                result.setdefault(str(aux[1]), {})[str(aux[0]).replace('\t', ' ')] = str(aux[2]).replace('\n', '')
                if str(aux[1]) not in list:
                    list.append(str(aux[1]))


    data = read_input(sys.stdin)
    for line in data:
        res = line.split(';')
        try:
            res2 = all_matching_cidrs(res[1], list)
            if res2 != '[]':
                sys.stdout.write('%s;%s\n' % (line.replace('\n',''),
                                            str(result[str(res2).split("'")[1]]).split("'")[1] + ';' +
                                            str(result[str(res2).split("'")[1]]).split("'")[3]))
        except:
            sys.stdout.write('%s;%s\n' % (line.replace('\n',''), "SIN COINCIDENCIA"))


if __name__ == "__main__":
    main()