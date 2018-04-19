#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `docker_compose_cleanup` package."""


import unittest
from click.testing import CliRunner

from docker_compose_cleanup import cli


class TestDocker_compose_cleanup(unittest.TestCase):
    """Tests for `docker_compose_cleanup` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_command_line_interface(self):
        """Test the CLI."""
        runner = CliRunner()
        result = runner.invoke(cli.main)
        assert result.exit_code == 0

        help_result = runner.invoke(cli.main, ['--help'])
        assert help_result.exit_code == 0
        assert '--version  Show the version and exit.' in help_result.output
        assert '--help     Show this message and exit.' in help_result.output

        help_result = runner.invoke(cli.main, ['remove'])
        assert help_result.exit_code == 2
        assert 'Error: Got unexpected extra argument' in help_result.output
