#!/usr/bin/env python
__author__ = 'victor'

import sys
import os


for line in sys.stdin:
    try:
        input_file = os.environ['map_input_file']
    except KeyError:
        input_file = os.environ['mapreduce_map_input_file']
    sys.stdout.write('%s\t\t%d\n' % (input_file, 1))