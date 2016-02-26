#!/usr/bin/env python
__author__ = 'victor'

import sys
import re
import os
from datetime import datetime


# global result
# result = {}


def hourcompare (ip, ref):  # DevolverÃ¡ la hora de asignaciÃ³n MAC anterior al acceso mÃ¡s cercana
    aux = 0.0
    first = True
    resultado = None
    dateref = datetime.strptime(ref, "%b %d %H:%M:%S")
    for hora in result[ip]:
        datedic = datetime.strptime(hora, "%b %d %H:%M:%S")
        if (datedic <= dateref and (dateref - datedic).total_seconds() < aux) or (datedic <= dateref and first):
            aux = (dateref - datedic).total_seconds()
            resultado = hora
            first = False
    return resultado


def read_input(file):
    # part2 = [
    #     r'(?P<month>\S+)',
    #     r'(?P<day>\S+)',
    #     r'(?P<hour>\S+)',
    #     r'.+',
    #     r'(DHCPACK)',
    #     r'.+',
    #     r'(?P<ip>[0-9]+(?:\.[0-9]+){3})',
    #     r'.+',
    # ]
    # pattern2 = re.compile(r'\s+'.join(part2)+r'\s*\Z')
    for line in file:
        # try:
        #     dhcp = re.search('(dhcpd\[[0-9]{0,10}\])', line)
        # except:
        #     continue
        # if dhcp:
        #     if "DHCPACK" in line:
        #         try:
        #             mac = re.search('[a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}', line)
        #             m = pattern2.match(line)
        #             res = m.groupdict()
        #             result.setdefault(res["ip"], {})[res["month"] + ' ' + res["day"] + ' ' + res["hour"]] = str(mac.group(0))
        #         except:
        #             sys.stdout.write('ERROR: ' + line)
        #             continue
        # else:
        #     yield line
            # continue
        yield line



def main():

    parts = [
        r'(?P<month>\S+)',
        r'(?P<day>\S+)',
        r'(?P<hour>\S+)',
        r'\S+',
        r'\S+',
        r'(?P<ip>\S+)',
        r'.+',
    ]

    pattern = re.compile(r'\s+'.join(parts)+r'\s*\Z')
    data = read_input(sys.stdin)

    global result
    result = {}
    with open("dhcp.txt", 'r') as f:
        for line in f:
            if line != "":
                aux = line.split('\t')
                result.setdefault(str(aux[0]), {})[str(aux[1])] = str(aux[2])

    for line in data:
        res = pattern.match(line).groupdict()
        if str(res["ip"]) in result:  # Si existe una asignaciÃ³n de esa IP a una MAC
            hora = hourcompare(res["ip"], res["month"] + ' ' + res["day"] + ' ' + res["hour"])
            if hora is not None:
                sys.stdout.write('%s;%s' % (res["month"] + ' ' + res["day"] + ' ' + res["hour"] + ';'
                                            + res["ip"], result[res["ip"]][hora]))

    sys.stdout.write(os.environ["mapreduce_job_id"].split("_")[-1])



if __name__ == "__main__":
    main()