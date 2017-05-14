#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from ippy import ippy
import sys


def main():
    ippt = ippy.Ippy()
    ippt.set_config(True, 'csv', 4)
    ippt.set_file(file='ip_list.csv')
    ippt.run()
    output = ippt.result()
    print(output)

if __name__ == "__main__":
    sys.exit(main())
