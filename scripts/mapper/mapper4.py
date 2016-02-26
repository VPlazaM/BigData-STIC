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


def between(month, day, hour):
    if beg[1] == month == end[1] and beg[2] <= day <= end[2] and beg[3] <= hour <= end[3]:
        return True
    return False


def setlimit():
    global beg
    beg = []
    global end
    end = []
    with open("filtro.txt", 'r') as f:
        for line in f:
            if not beg:
                beg = line.split()
            else:
                end = line.split()




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
    setlimit()
    data = read_input(sys.stdin)


    for line in data:
        res = pattern.match(str(line)).groupdict()
        if between(res["month"], res["day"], res["hour"]):
            res2 = res["month"] + '\t' + res["day"] + '\t' + res["hour"][:2] + '\t' + res["ip"] + '\t\t' + res["path"]
            sys.stdout.write('%s\t\t%d\n' % (res2, 1))
        else:
            continue

if __name__ == "__main__":
    main()