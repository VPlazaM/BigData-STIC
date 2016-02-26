#!/usr/bin/env python
__author__ = 'victor'


import sys
import re


def main():
    result = {}

    for line in sys.stdin:
        part2 = [
            r'(?P<month>\S+)',
            r'(?P<day>\S+)',
            r'(?P<hour>\S+)',
            r'.+',
            r'(DHCPACK)',
            r'.+',
            r'(?P<ip>[0-9]+(?:\.[0-9]+){3})',
            r'.+',
        ]
        pattern2 = re.compile(r'\s+'.join(part2)+r'\s*\Z')

        if "DHCPACK" in line:
            try:
                mac = re.search('[a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}[:][a-fA-F0-9]{2}', line)
                m = pattern2.match(line)
                res = m.groupdict()
                result.setdefault(str(res["ip"]), {})[res["month"] + ' ' + res["day"] + ' ' + res["hour"]] = str(mac.group(0))
            except:
                continue

    for dato in result:
        for dato2 in result[dato]:
            sys.stdout.write('%s\t\t%d\n' % (str(dato) + ';' + str(dato2) + ';' + str(result[dato][dato2]), 1))


if __name__ == "__main__":
    main()