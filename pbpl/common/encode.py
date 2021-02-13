#!/usr/bin/env python
import sys
import numpy as np
import toml
import argparse
import tempfile
import subprocess
from argparse import RawDescriptionHelpFormatter
import pbpl.common
from pbpl.common.units import *

def get_parser():
    parser = argparse.ArgumentParser(
        description='Encode',
        formatter_class=RawDescriptionHelpFormatter,
        epilog='''\
Example:
.. code-block:: sh

  pbpl-common-encode animate.toml
        ''')
    parser.add_argument(
        'config_filename', metavar='conf-file',
        help='Configuration file')
    return parser

def get_args():
    args = get_parser().parse_args()
    args.conf = toml.load(args.config_filename)
    return args

def main():
    args = get_args()
    conf = args.conf
    print('yo')


if __name__ == '__main__':
    sys.exit(main())
