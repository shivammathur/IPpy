#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future.standard_library import install_aliases
from ippy import ippy
import sys


def main():
    ippt = ippy.Ippy()
    ippt.set_config(True, 'json', 4)
    ippt.set_file(file='ip_list.csv')
    ippt.run()
    output = ippt.result()
    print(output)

if __name__ == "__main__":
    install_aliases()
    sys.exit(main())
