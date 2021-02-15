import re

import pytest
from click.testing import CliRunner

from stdclean.__main__ import main


@pytest.fixture(scope='session')
def cli_runner():
    """Fixture that returns a helper function to run the stdclean cli."""
    runner = CliRunner()

    def cli_main(*cli_args, **cli_kwargs):
        """Run stdclean cli main with the given args."""
        return runner.invoke(main, cli_args, **cli_kwargs)

    return cli_main


@pytest.fixture(params=['-V', '--version'])
def version_cli_flag(request):
    """Pytest fixture return both version invocation options."""
    return request.param


def test_cli_version(cli_runner, version_cli_flag):
    """Verify correct version output by stdclean on cli invocation."""
    result = cli_runner(version_cli_flag)
    assert result.exit_code == 0
    print('HERE: {}'.format(result.output))
    assert re.match('stdclean \\d\\.\\d\\.\\d from .+ \\(Python \\d\\.\\d\\)',
                    result.output)
