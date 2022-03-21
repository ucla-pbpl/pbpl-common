#!/usr/bin/env python
import os
import sys
import toml
import argparse
from argparse import RawDescriptionHelpFormatter
from tempfile import TemporaryDirectory
from concurrent.futures import ThreadPoolExecutor, as_completed
import pbpl.common

def get_parser():
    parser = argparse.ArgumentParser(
        description='Encode',
        formatter_class=RawDescriptionHelpFormatter,
        epilog='''\
Example:
.. code-block:: sh

  pbpl-common-encode encode.toml
        ''')
    parser.add_argument(
        'config_filename', metavar='conf-file',
        help='Configuration file')
    return parser

def get_args():
    args = get_parser().parse_args()
    args.conf = toml.load(args.config_filename)
    return args

def get_num_pdf_pages(filename):
    pdfinfo = os.popen(f'pdfinfo {filename}').readlines()
    prefix = 'Pages:'
    A = list(filter(lambda x: x.startswith(prefix), pdfinfo))
    return int(A[0][len(prefix):])

def main():
    args = get_args()
    conf = args.conf

    c = conf['Input']
    infile = c['Filename']
    c = conf['Output']
    outfile = c['Filename']
    dpi = c['DPI']
    fps = c['FPS']
    encoding = c['Encoding']

    num_pages = get_num_pdf_pages(infile)

    tmp = TemporaryDirectory()
    with ThreadPoolExecutor() as executor:
        def doit(page_number):
            cmd = f'pdftoppm -f {page_number+1} -l {page_number+1} '
            cmd += f'-r {dpi} -png '
            cmd += f'{infile} {tmp.name}/frame'
            os.system(cmd)

        futures = []
        for  i in range(num_pages):
            futures.append(executor.submit(doit, i))
        for future in as_completed(futures):
            future.result()

    num_chars = len(str(num_pages))
    cmd = f'ffmpeg -y -r {fps} -i {tmp.name}/frame-%0{num_chars}d.png '
    cmd += encoding + f' -r {fps} {outfile}'
    os.system(cmd)

if __name__ == '__main__':
    sys.exit(main())
