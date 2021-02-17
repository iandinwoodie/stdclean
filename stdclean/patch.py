"""Functions for patching target C++ source and header files."""

import re


def find_std_objects(std_objects, line):
    pattern = (
        r'\\"|"(?:\\"|[^"])*"|((^|[^\w:])({objects})((?=<)|$|[^\w]))'.format(
            objects='|'.join(std_objects)))
    matches = re.findall(pattern, line)
    return set([x[2] for x in matches if x[2] != ''])


def build_std_decl_lines(objects):
    # TODO: account for existing decls
    std_decl = 'using std::{obj};\n'
    return [std_decl.format(obj=x) for x in objects]


def patch_with_std_decl(path, mapping):
    with open(path, 'r') as fp:
        lines = fp.readlines()
    include_directive = '#include '
    last_include_pos = 0
    line_comment_delim = '//'
    block_comment_open_delim = '/*'
    block_comment_close_delim = '*/'
    inside_block_comment = False
    std_objects = set().union(*mapping.values())
    found_objects = set()
    for idx, line in enumerate(lines):
        if block_comment_close_delim in line:
            inside_block_comment = False
            continue
        elif inside_block_comment:
            continue
        elif block_comment_open_delim in line:
            inside_block_comment = True
            continue
        elif include_directive in line:
            last_include_pos = idx
            continue
        elif line_comment_delim in line:
            continue
        elif not len(line) > 1:
            continue
        found_objects.update(find_std_objects(std_objects, line))
    if not found_objects:
        return
    decl_lines = build_std_decl_lines(found_objects)
    print(decl_lines)
    for line in decl_lines:
        lines.insert(last_include_pos+1, line)
    # with open(path, 'w') as fp:
    #    fp.writelines(lines)
