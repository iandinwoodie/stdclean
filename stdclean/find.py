"""Functions for finding target C++ source and header files."""

from pathlib import Path


def find_cpp_file_paths(target):
    """Determine C++ source and header file paths corresponding to the target.

    :param target: Source file or directory.
    :returns path_list: List of located C++ source and header Path objects.
    """
    target_path = Path(target)
    # TODO: Allow users to configure file extensions without needing to modify
    # the tool's source code.
    file_exts = (
        '.cpp', '.cc', '.C', '.cxx', '.c++',
        '.h', '.hpp', '.h', '.H', '.hxx', '.h++'
    )
    path_list = []
    if not target_path.exists():
        raise RuntimeError('Target path "{}" does not exist.'.format(target))
    elif target_path.is_dir():
        for ext in file_exts:
            path_list.extend(target_path.rglob('*{}'.format(ext)))
    else:
        path_list.append(target_path)
    return path_list
