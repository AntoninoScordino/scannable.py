#
# Copyright (C) 2023 Antonino Scordino <a.scordino.07@gmail.com>
#
# SPDX-License-Identifier: WTFPL
#

import argparse
from utils.generate import Generate

parser = argparse.ArgumentParser(prog='scannable.py',
                                 description='Generate Spotify scannable code through a Python script.')
parser.add_argument('link', help='Spotify link to generate a scannable image from', default=None)
parser.add_argument('-f', '--format', help='file format for the scannable output', default='png')
parser.add_argument('-b', '--background', help='background color for the scannable output', default='000000')
parser.add_argument('-t', '--text', help='text color for the scannable output', default='white')
parser.add_argument('-s', '--size', help='size of the scannable output', default='512')

args = parser.parse_args()

def main():
    scannable = Generate(args.format, args.background, args.text, args.size, args.link)

if __name__ == '__main__':
    main()