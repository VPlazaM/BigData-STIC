#!/usr/bin/env python
__author__ = 'victor'

import sys


def read_mapper_output(file):
    for line in file:
        yield line


def main(separator='\t\t'):
    data = read_mapper_output(sys.stdin)
    for line in data:
        print(line)

if __name__ == "__main__":
    main()