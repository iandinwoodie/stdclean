"""Tests for stdclean.find module."""

import os

import pytest

from stdclean import find


@pytest.fixture(params=['test-find'])
def target_dir(request):
    """Fixture returning path for test_find_cpp_file_paths test."""
    return os.path.join('tests', request.param)


def test_find_cpp_file_paths(target_dir):
    """Verify correctness of find.find_cpp_file_paths path detection."""
    path_list = find.find_cpp_file_paths(target=target_dir)
    assert len(path_list) == 10
