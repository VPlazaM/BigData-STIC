#!/usr/bin/env python
__author__ = 'victor'

import sys
import re


def read_input(file):
    for line in file:
        yield line


def main():
    parts = [
        r'(?P<month>\S+)',
        r'(?P<day>\S+)',
        r'(?P<hour>\S\S)\S+',
        r'\S+',
        r'\S+',
        r'(?P<ip>\S+)',
        r'.+',
    ]
    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')

    data = read_input(sys.stdin)
    for line in data:
        res = pattern.match(str(line)).groupdict()
        sys.stdout.write('%s\t\t%d\n' % (res["month"] + '\t' + res["day"] + '\t' + res["hour"] + '\t' + res["ip"], 1))

if __name__ == "__main__":
    main()