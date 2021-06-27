"""Functions for patching target C++ source and header files."""

import re


def find_std_objects(std_objects, line):
    delims = r'\s|\(|\)|<|>|&|\*'
    segments = re.split(delims, line)
    return set([x for x in segments if x in std_objects])


def get_std_decl_lines(objects):
    # TODO: account for existing decls
    std_decl = 'using std::{obj};\n'
    return set(std_decl.format(obj=x) for x in objects)


def has_nonquoted_instance(line, obj):
    regex = re.compile(
        r'{obj}(?=([^"\\]*(\\.|"([^"\\]*\\.)*[^"\\]*"))*[^"]*$)'.format(
            obj=obj))
    return True if regex.search(line) else False


def patch_with_std_decl(lines, mapping):
    last_include_pos = 0
    inside_block_comment = False
    std_objects = set().union(*mapping.values())
    found_objects = set()
    std_directive_removed = False
    existing_decl_lines = set()
    for idx, line in enumerate(lines):
        # Check if a block comment is being closed.
        if '*/' in line:
            # Note: this means we don't support `string s; /* comment ...`
            inside_block_comment = False
            continue
        # Check if the line is within an open block comment.
        elif inside_block_comment:
            continue
        # Perform no further checks for single line comments or empty lines.
        elif '//' in line or line.strip() == '':
            # Note: this means we don't support `string s; // comment`
            continue
        elif '/*' in line:
            # Note: this means we don't support `... comment */ string s;`
            inside_block_comment = True
            continue
        elif '#include' in line:
        #elif has_nonquoted_instance(line, '#include'):
            last_include_pos = idx
            continue
        elif 'using namespace std;' in line:
            std_directive_removed = True
            lines[idx] = ''
            continue
        elif 'using std::' in line:
            existing_decl_lines.add(line)
            continue
        found_objects.update(find_std_objects(std_objects, line))
    new_decl_lines = get_std_decl_lines(found_objects) - existing_decl_lines
    new_decl_lines = list(new_decl_lines).sort()
    print(new_decl_lines)
    # Return early if no modifications are required.
    if not (new_decl_lines or std_directive_removed):
        return []
    [lines.insert(last_include_pos+1, x) for x in new_decl_lines]
    return lines
