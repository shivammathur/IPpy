#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ippy
----------------------------------

Tests for `ippy` module.
"""

import pytest
from ippy import ippy
import sys
import os
import json
from io import StringIO
from csv import reader


def test_config():
    ippt = ippy.Ippy()
    ippt.set_config(verbose_mode=False, output_mode='csv', num_workers=10)

    assert ippt.verbose is False
    assert ippt.output == 'csv'
    assert ippt.num_workers == 10


def test_set_file():
    ippt = ippy.Ippy()
    pytest.raises(Exception, "ippt.set_file()")
    ippt.set_file('testfile')

    assert ippt.file == 'testfile'


def test_ping_args():
    ippt = ippy.Ippy()

    ping_args = ippt.get_ping_args("Windows")
    assert ping_args == ["ping", "-n", "2", "-l", "1", "-w", "2000"]

    ping_args = ippt.get_ping_args("Linux")
    assert ping_args == ["ping", "-c", "2", "-l", "1", "-s", "1", "-W", "2"]

    pytest.raises(ValueError, "ippt.get_ping_args('Test')")


def test_filepath():
    ippt = ippy.Ippy()
    pytest.raises(Exception, "ippt.get_filepath()")

    ippt.set_file('testfile')
    file_path = ippt.get_filepath()

    assert file_path == os.path.join(sys.path[0], "testfile")


def test_run():
    ippt = ippy.Ippy()
    ippt.set_config(True, 'csv', 10)
    ippt.set_file(file='ip_list.csv')
    ippt.run()

    assert property(ippt.get_accessible) is not None
    assert property(ippt.get_not_accessible) is not None
    assert property(ippt.get_results) is not None


def test_empty_result():
    ippt = ippy.Ippy()
    ippt.set_config(False, 'test', 10)
    ippt.set_file(file='ip_list.csv')
    ippt.run()
    pytest.raises(ValueError, "ippt.result()")

def test_json_result():
    ippt = ippy.Ippy()
    ippt.set_config(False, 'json', 10)
    result = ippt.result()
    assert json.loads(result) is not None

def test_csv_result():
    ippt = ippy.Ippy()
    ippt.set_config(False, 'csv', 10)
    result = ippt.result()
    my_result = StringIO(result)
    my_reader = reader(my_result, delimiter=',')
    csv_result = ''
    for row in my_reader:
        for cell in row:
            csv_result += cell
        csv_result += '\n'

    csv_result = csv_result.replace(',', '').replace('\n', '')
    result = result.replace(',', '').replace('\n', '').replace('\r', '')

    assert csv_result == result
