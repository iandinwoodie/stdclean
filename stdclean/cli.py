"""Main stdclean command line interface (CLI)."""

import os
import sys

import click

from stdclean import __version__




def get_version_msg():
    """Return the stdclean version, location, and Python executing it."""
    python_version = sys.version[:3]
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    message = 'stdclean {} from {} (Python {})'
    return message.format(__version__, location, python_version)


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-V', '--version', message=get_version_msg())
@click.argument('target', required=True)
def main():
    print(target)


if __name__ == '__main__':
    main()
