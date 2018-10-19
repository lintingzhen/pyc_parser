#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Create Date: 2018-10-19 10:39
# Author: Airlam

import imp
import sys


def generate_pyc(name):
    fp, pathname, description = imp.find_module(name)
    try:
        imp.load_module(name, fp, pathname, description)
    finally:
        if fp:
            fp.close()

if __name__ == '__main__':
    generate_pyc(sys.argv[1])
