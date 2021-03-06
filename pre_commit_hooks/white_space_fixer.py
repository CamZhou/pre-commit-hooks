from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import argparse
import io


def fix_strings(filename):
    contents = io.open(filename).read()
    contents_copy = contents
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

    for key in replacement_dict.keys():
        for line in contents_copy.splitlines():
            if key in line:
                line = line.replace(key, replacement_dict[key])
            new_contents += line + '\n'
        contents_copy = new_contents
        new_contents = ''

    if contents != contents_copy:
        with io.open(filename, 'w') as write_handle:
            write_handle.write(contents_copy)
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
