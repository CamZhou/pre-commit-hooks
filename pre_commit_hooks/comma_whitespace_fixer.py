from __future__ import print_function

import fileinput
import re
import sys

import argparse

from pre_commit_hooks.util import cmd_output


def _fix_file(filename, markdown=False):
    for line in fileinput.input([filename], inplace=True):
        # list of string matches
        matches = re.findall(',^[[:space:]]')

        for match in matches:
            re.replace(match, match[0] + " " + match[-1], line)

        print(line)


def fix_comma_whitespace(argv=None):
    parser = argparse.ArgumentParser()
    args = parser.parse_args(argv)

    bad_comma_whitespace_files = cmd_output(
        'grep', '-l', ',^[[:space:]]', *args.filenames, retcode=None
    ).strip().splitlines()

    if bad_comma_whitespace_files:
        for bad_comma_whitespace_file in bad_comma_whitespace_files:
            print('Fixing {0}'.format(bad_comma_whitespace_file))
            _fix_file(bad_comma_whitespace_file)
        return 1
    else:
        return 0


if __name__ == '__main__':
    sys.exit(fix_comma_whitespace())
