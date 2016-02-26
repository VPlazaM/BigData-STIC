#!/usr/bin/env python
__author__ = 'victor'

import sys
import os

current_path = None
path = None
filepath = None
filename = None
current_count = 0
total_count = 0
dic = {}

# input comes from STDIN
for line in sys.stdin:

    line = line.strip()
    path, count = line.split('\t\t', 1)

    if current_path == path:
        current_count += int(count)
    else:
        if current_path:
            filepath, filename = os.path.split(current_path) #para quedarse solo con el nombre del fichero, no la ruta
            dic[filename] = current_count
            #dic[str(current_path)] = current_count
            total_count += current_count
        current_count = int(count)
        current_path = path

if current_path == path:
    filepath, filename = os.path.split(current_path)
    dic[filename] = current_count
    #dic[str(path)] = current_count
    total_count += current_count


for k, v in dic.items():
    sys.stdout.write(k + '\t' + str(v) + '\n')
sys.stdout.write("Total de lineas:" + '\t' + str(total_count) + '\n')