"""Test to cover daeclipse library."""

from daeclipse_cli import __version__


def test_version():
    """Test daeclipse library version."""
    assert __version__ == '0.0.1'
