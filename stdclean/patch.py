"""Functions for patching target C++ source and header files."""

import re

STD_LIB_MAPPING = {
    'bitset': [
        'bitset',
    ],
    'string': [
        'basic_string',
        'string',
        'u8string',
        'u16string',
        'u32string',
        'wstring',
    ],
    'vector': [
        'vector',
    ]
}


def find_std_objects(std_objects, line):
    pattern = r'\\"|"(?:\\"|[^"])*"|((^|[\s<(])({objects})([\s>),])?)'.format(
        objects='|'.join(std_objects))
    matches = re.findall(pattern, line)
    return set([x[2] for x in matches if x[2] != ''])


def add_using_declarations(path, mapping=STD_LIB_MAPPING):
    print(path)
    with open(path, 'r') as fp:
        lines = fp.readlines()
    std_objects = set().union(*STD_LIB_MAPPING.values())
    include_directive = '#include '
    line_comment_delim = '//'
    block_comment_open_delim = '/*'
    block_comment_close_delim = '*/'
    inside_block_comment = False
    found_objects = set()
    for line in lines:
        if block_comment_close_delim in line:
            inside_block_comment = False
            continue
        elif inside_block_comment:
            continue
        elif block_comment_open_delim in line:
            inside_block_comment = True
            continue
        elif include_directive in line:
            continue
        elif line_comment_delim in line:
            continue
        elif not len(line) > 1:
            continue
        found_objects.update(find_std_objects(std_objects, line))
    if found_objects:
        print('found std objects: {}'.format(found_objects))
