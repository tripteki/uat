import unittest
import pytest
import pexpect
from abc import ABC

class TestCase (ABC, unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """
        self.driver = pexpect

        yield

        self.driver = None
