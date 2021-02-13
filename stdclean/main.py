"""Main entry point for the stdclean command."""

import os


def stdclean(target):
    if not os.path.exists(target):
        raise RuntimeError('Target path "{}" does not exist.'.format(target))

