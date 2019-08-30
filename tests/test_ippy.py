#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ippy
----------------------------------

Tests for `ippy` module.
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future.standard_library import install_aliases
from ippy import ippy
import pytest
import sys
import os
import json
from io import StringIO
from csv import reader
install_aliases()


def test_config():
    ippy_obj = ippy.Ippy()
    ippy_obj.set_config(verbose_mode=False, output_mode='csv', num_workers=10)

    assert ippy_obj.verbose is False
    assert ippy_obj.output == 'csv'
    assert ippy_obj.num_workers == 10


def test_set_file():
    ippy_obj = ippy.Ippy()
    with pytest.raises(Exception):
        ippy_obj.set_file()
    ippy_obj.set_file('testfile')

    assert ippy_obj.file == 'testfile'


def test_ping_args():
    ippy_obj = ippy.Ippy()

    ping_args = ippy_obj.get_ping_args("Windows")
    assert ping_args == ["ping", "-n", "2", "-l", "1", "-w", "2000"]

    ping_args = ippy_obj.get_ping_args("Linux")
    assert ping_args == ["ping", "-c", "2", "-l", "1", "-s", "1", "-W", "2"]

    ping_args = ippy_obj.get_ping_args("Darwin")
    assert ping_args == ["ping", "-c", "2", "-l", "1", "-s", "1", "-W", "2000"]

    with pytest.raises(ValueError):
        ippy_obj.get_ping_args('Test')


def test_filepath():
    ippy_obj = ippy.Ippy()
    with pytest.raises(Exception):
        ippy_obj.get_filepath()

    ippy_obj.set_file('testfile')
    file_path = ippy_obj.get_filepath()

    assert file_path == os.path.join(sys.path[0], "testfile")


def test_run():
    ippy_obj = ippy.Ippy()
    ippy_obj.set_config(True, 'csv', 10)
    ippy_obj.set_file(file='ip_list.csv')
    ippy_obj.run()

    assert property(ippy_obj.get_accessible) is not None
    assert property(ippy_obj.get_not_accessible) is not None
    assert property(ippy_obj.get_results) is not None


def test_empty_result():
    ippy_obj = ippy.Ippy()
    ippy_obj.set_config(False, 'test', 10)
    ippy_obj.set_file(file='ip_list.csv')
    ippy_obj.run()
    with pytest.raises(ValueError):
        ippy_obj.result()


def test_json_result():
    ippy_obj = ippy.Ippy()
    ippy_obj.set_config(False, 'json', 10)
    result = ippy_obj.result()
    assert json.loads(result) is not None


def test_csv_result():
    ippy_obj = ippy.Ippy()
    ippy_obj.set_config(False, 'csv', 10)
    ippy_obj.set_file(file='ip_list.csv')
    ippy_obj.run()
    result = ippy_obj.result()
    my_result = StringIO(result)
    my_reader = reader(my_result, delimiter=str(','))
    csv_result = ''
    for row in my_reader:
        for cell in row:
            csv_result += cell
        csv_result += '\n'

    csv_result = csv_result.replace(',', '').replace('\n', '')
    result = result.replace(',', '').replace('\n', '').replace('\r', '')

    assert csv_result == result
