#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Python script to check if IP address and domains are accessible or not.
.. codeauthor:: Shivam Mathur <shivam_jpr@hotmail.com>
"""

from io import StringIO
from json import dumps
from csv import writer
from itertools import zip_longest

import sys
import os
import platform
import subprocess
import threading
import queue
import pingparsing


class Ippy(object):
    def __init__(self, verbose_mode=True, output_mode='json', num_workers=4, file=None):
        # Modes
        self.verbose = verbose_mode
        self.output = output_mode

        # The number of workers.
        self.num_workers = num_workers

        # Input file
        self.file = file

        # Private members
        self._pending = queue.Queue()
        self._done = queue.Queue()
        self._workers = []
        self._results = []
        self._accessible = []
        self._not_accessible = []

    @property
    def get_results(self):
        return self._results

    @property
    def get_accessible(self):
        return self._accessible

    @property
    def get_not_accessible(self):
        return self._not_accessible

    def set_config(self, verbose_mode=True, output_mode='json', num_workers=4):

        """ Function to set the configuration of IPpy
        :param verbose_mode: Print ping output if True.
        :param output_mode: Output mode of the results. Supported - 'json' or 'csv'.
        :param num_workers: Number of workers to ping.
        """
        self.verbose = verbose_mode
        self.output = output_mode
        self.num_workers = num_workers

    def set_file(self, file=None):
        """ Function to set the input file.
        :param file: Input filename.
        """
        if file is None:
            raise Exception("No input file specified.")
        else:
            self.file = file

    @staticmethod
    def get_ping_args(platform_os=None):
        """
        :return ping_args: ping command with arguments
        """

        plat = platform.system()

        if platform_os is not None:
            plat = platform_os

        # The arguments for the 'ping', excluding the address.
        if plat == "Windows":
            ping_args = ["ping", "-n", "2", "-l", "1", "-w", "2000"]
        elif plat == "Linux":
            ping_args = ["ping", "-c", "2", "-l", "1", "-s", "1", "-W", "2"]
        else:
            raise ValueError("Unknown platform")

        return ping_args

    def get_filepath(self):
        """
        :return file_path: Returns absolute path of the Input file.
        """
        if self.file is None:
            raise Exception("No input file specified.")
        script_dir = sys.path[0]
        file_path = os.path.join(script_dir, self.file)
        return file_path

    @staticmethod
    def worker_func(ping_args, pending, done):
        """ Function to perform the actual ping.
        :param ping_args: Ping arguments
        :param pending: Pending queue
        :param done: Done queue
        """
        try:
            while True:
                # Get the next address to ping.
                address = pending.get_nowait()

                ping = subprocess.Popen(ping_args + [address],
                                        stdout=subprocess.PIPE,
                                        stderr=subprocess.PIPE
                                        )
                out, error = ping.communicate()

                # Output the result to the 'done' queue.
                done.put(({'result': out, 'ip': address}, error))
        except queue.Empty:
            # No more addresses.
            pass
        finally:
            # Tell the main thread that a worker is about to terminate.
            done.put(None)

    def run(self):
        """ Function to put everything together and parse the ping outputs.
        """
        ping_args = self.get_ping_args()
        file_path = self.get_filepath()

        for _ in range(self.num_workers):
            self._workers.append(threading.Thread(target=self.worker_func, args=(ping_args, self._pending, self._done)))

        # Put all the addresses into the 'pending' queue.
        with open(file_path, "r") as hostsFile:
            for line in hostsFile:
                self._pending.put(line.strip())

        # Start all the workers.
        for w in self._workers:
            w.daemon = True
            w.start()

        # Parser to parse the ping response
        ping_parser = pingparsing.PingParsing()

        # Get the results as they arrive.
        num_terminated = 0
        while num_terminated < self.num_workers:
            result = self._done.get()
            if result is None:
                # A worker is about to terminate.
                num_terminated += 1
            else:
                # Print as soon as results arrive
                if result[1].decode("utf-8") == '':  # Error is empty string
                    if self.verbose:
                        print("IP", result[0]['ip'])
                        print(result[0]['result'].decode("utf-8"))
                    ping_parser.parse(result[0]['result'].decode("utf-8"))
                    if int(ping_parser.packet_loss) == 100:  # All packets are lost
                        self._not_accessible.append(result[0]['ip'])
                    else:
                        self._accessible.append(result[0]['ip'])
                self._results.append(result)

        # Wait for all the workers to terminate.
        for w in self._workers:
            w.join()

    def result(self):
        """ Function to encode the output into the specified output mode.
        :return result: The output string in the specified output mode.
        """
        if self.output == 'json':
            result_dict = {"Accessible": self._accessible, "Not Accessible": self._not_accessible}
            result = dumps(result_dict, indent=4)
        elif self.output == 'csv':
            result = StringIO()
            writer(result)
            result = result.getvalue().strip('\r\n')
            result = 'Accessible,Not Accessible\n' + result
        else:
            raise ValueError("Unknown output mode")

        return result
