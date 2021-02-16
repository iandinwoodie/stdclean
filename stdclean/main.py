"""Main entry point for the stdclean command."""

from stdclean.find import find_cpp_file_paths
from stdclean.patch import add_using_declarations


def stdclean(target):
    path_list = find_cpp_file_paths(target)
    for path in path_list:
        add_using_declarations(path)
