import os
import sys
import argparse

#from stdclean import __version__
__version__ = 0


def version_msg():
    """Return the stdclean version, location, and Python executing it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = 'stdclean {} from {} (Python {})'
    return message.format(__version__, location, python_version)


def main():
    parser = argparse.ArgumentParser(prog='stdclean')
    parser.add_argument(
        '--version', action='version', version=version_msg())
    args = parser.parse_args()
    print(args)


if __name__ == '__main__':
    main()
