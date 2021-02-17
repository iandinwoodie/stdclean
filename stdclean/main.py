"""Main entry point for the stdclean command."""

from stdclean.find import find_cpp_file_paths
from stdclean.patch import patch_with_std_decl


def stdclean(target):
    path_list = find_cpp_file_paths(target)
    for path in path_list:
        print(path)
        patch_with_std_decl(path)
