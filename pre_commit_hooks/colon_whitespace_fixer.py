from __future__ import print_function

import argparse
import fileinput
import os
import sys
import re

from pre_commit_hooks.util import cmd_output


def fix_file(filename):
    for line in fileinput.input([filename], inplace=True):
        # preserve trailing two-space for non-blank lines in markdown files
            #if 'where' in line:
                # if there is space btw : and var name
                line = re.sub(r':\s+', ':', line)
    print(line.rstrip())

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    ret = 0

    for filename in args.filenames:
        file = fix_file(filename)
        if file != 0:
            print('Fixing strings in {0}'.format(filename))
        ret |= file

    return ret