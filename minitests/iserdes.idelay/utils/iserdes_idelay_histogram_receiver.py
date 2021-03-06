#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (C) 2017-2020  The Project X-Ray Authors.
#
# Use of this source code is governed by a ISC-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/ISC
#
# SPDX-License-Identifier: ISC
"""
This script receives and parses data generated by the "histogram" test design.
"""

import argparse
import serial

# =============================================================================


def main():

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("port", type=str, help="Serial port name")
    parser.add_argument("--baud", type=int, default=115200, help="Baudrate")

    args = parser.parse_args()

    # Open serial port
    port = serial.Serial(args.port, baudrate=args.baud)

    # Get first line and discard it. It may be broken
    port.readline()

    # Read and process lines
    while True:

        line = port.readline()
        line = line.decode("ASCII").strip()

        data = [int(x, base=16) for x in line.split("_")]
        print(" ".join("%4d" % x for x in data))


# =============================================================================

if __name__ == "__main__":
    main()
