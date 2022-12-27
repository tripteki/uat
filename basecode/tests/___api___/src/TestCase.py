import unittest
import pytest
from abc import ABC
from aiohttp import ClientSession as Aio

class TestCase (ABC, unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """
        self.driver = Aio

        yield

        self.driver = None
