#!/usr/bin/env python
__author__ = 'victor'

from operator import itemgetter
from itertools import groupby
import sys

def read_mapper_output(file, separator='\t\t'):
    for line in file:
        yield line.rstrip().split(separator, 1)


def main(separator='\t\t'):
    data = read_mapper_output(sys.stdin, separator=separator)
    data = sorted(data, key=itemgetter(0))

    for current_key, group in groupby(data, itemgetter(0)):
        total_count = sum(int(count) for current_key, count in group)
        sys.stdout.write("%s\t%s\n" % (current_key, total_count))


if __name__ == "__main__":
    main()
	