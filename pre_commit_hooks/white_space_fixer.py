from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io


def fix_strings(filename):
    contents = io.open(filename).read()
    new_contents = ''

    replacement_dict = {
        'if(': 'if (',
        'else(': 'else (',
        'while(': 'while (',
        'for(': 'for (',
        'try{': 'try {',
        'catch(': 'catch (',
        '){': ') {',
    }

    for line in contents.splitlines():
        for key in replacement_dict.keys():
            if key in line:
                line = line.replace(key, replacement_dict[key])
                new_contents += line
        new_contents += line

    if contents != new_contents:
        with io.open(filename, 'w') as write_handle:
            write_handle.write(new_contents)
        return 1
    else:
        return 0


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to fix')
    args = parser.parse_args(argv)

    retv = 0

    for filename in args.filenames:
        return_value = fix_strings(filename)
        if return_value != 0:
            print('Fixing strings in {0}'.format(filename))
        retv |= return_value

    return retv
