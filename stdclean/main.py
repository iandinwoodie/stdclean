"""Main entry point for the stdclean command."""

from stdclean.find import find_cpp_file_paths


def stdclean(target):
    path_list = find_cpp_file_paths(target)
    [print(p) for p in path_list]
