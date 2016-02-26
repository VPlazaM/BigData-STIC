#!/usr/bin/env python
__author__ = 'victor'

import sys
import re
import os

def read_input(file):
    for line in file:
        try:
            input_file = os.environ['mapreduce_map_input_file']
        except KeyError:
            input_file = os.environ['map_input_file']
        a, b = os.path.split(input_file)
        custom_input = "/" + os.path.basename(a) + "/" + b + " " + str(line)
        yield custom_input


# (?:80)\s(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b

def setorigin():
    global origin
    origin = {}
    with open("origenes.txt", 'r') as f:
        for line in f:
            aux = line.split()
            aux2 = aux[0].split('x')[0]
            if aux2 != "Resto":
                origin.setdefault(aux2, aux[1])



def getorigin(ip):
    for semiip in origin:
        if semiip[0] != '*' and ip.startswith(semiip):
            return origin[semiip]
        if semiip[0] == '*' and ip.endswith(semiip):
            return origin[semiip]
    return 'Externo'





def main():
    parts = [
        r'(?P<path>\S+)',
        r'(?P<month>\S+)',
        r'(?P<day>\S+)',
        r'(?P<hour>\S+)',
        r'\S+',
        r'\S+',
        r'(?P<ip>\S+)',
        r'.+',
    ]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    setorigin()
    data = read_input(sys.stdin)
    first = True
    for line in data:
        res = pattern.match(str(line)).groupdict()
        if first:
            for type in origin:
                sys.stdout.write('%s\t\t%d\n' % (res["month"] + ';' + res["day"] + ';' + res["hour"][:2] + '\t\t' + origin[type], 0))
            first = False
        res2 = res["month"] + ';' + res["day"] + ';' + res["hour"][:2] + '\t\t' + getorigin(res["ip"])
        sys.stdout.write('%s\t\t%d\n' % (res2, 1))


if __name__ == "__main__":
    main()