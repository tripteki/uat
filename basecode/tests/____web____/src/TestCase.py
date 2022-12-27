import unittest
import pytest
from ....src.Helpers.LogNameSpace import log_name_space
from abc import ABC
from os import environ
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class TestCase (ABC, unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """
        options = Options ()
        options.add_argument ("--disable-extensions")
        options.add_argument ("--disable-gpu")
        options.add_argument ("--no-sandbox")
        options.add_argument ("--headless")

        self.driver = webdriver.Chrome (service = ChromeService (ChromeDriverManager ().install (), service_args = ["--verbose", "--log-path=" + environ.get ("WEBTEST_LOGFILE", log_name_space ("web"))]), options = options)

        yield

        self.driver.quit ()
