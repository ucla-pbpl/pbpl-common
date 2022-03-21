#!/usr/bin/env python
import sys
import argparse
from argparse import RawDescriptionHelpFormatter
import os
import re

def get_parser():
    parser = argparse.ArgumentParser(
        description='Concatenate STL files',
        formatter_class=RawDescriptionHelpFormatter,
        epilog='''\
Example:
.. code-block:: sh

  pbpl-common-stl-cat 000.stl 001.stl 002.stl foo.stl:bar > out.stl
        ''')
    parser.add_argument(
        'solids', metavar='STLFILE[:SOLID]', nargs='+',
        help='input solids')
    return parser

def get_args():
    args = get_parser().parse_args()
    return args

def dump_one(fout, text, solid_name):
    pattern = re.compile('(solid)(\s+facet.+?endsolid)', re.DOTALL)
    m = re.search(pattern, text)
    fout.write(
        m.group(1) + ' ' + solid_name + m.group(2) + ' ' + solid_name + '\n')

def dump_two(fout, text, solid_name):
    esc_name = re.escape(solid_name)
    pattern = re.compile(
        'solid\s+' + esc_name + '.+?endsolid\s+' + esc_name, re.DOTALL)
    m = re.search(pattern, text)
    fout.write(m.group())

def main():
    args = get_args()
    fout = sys.stdout
    for solid_spec in args.solids:
        solid_spec = solid_spec.split(':', 1)
        filename = solid_spec[0]
        with open(filename, 'r') as fin:
            text = fin.read()
        if len(solid_spec) == 1:
            solid_name = os.path.splitext(os.path.basename(filename))[0]
            dump_one(fout, text, solid_name)
        else:
            solid_name = solid_spec[1]
            dump_two(fout, text, solid_name)

if __name__ == '__main__':
    sys.exit(main())
