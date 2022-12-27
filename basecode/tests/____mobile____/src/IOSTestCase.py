import unittest
import pytest
from abc import ABC
from os import environ
from appium import webdriver
from appium.options.ios import XCUITestOptions

class IOSTestCase (ABC, unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """
        options = XCUITestOptions ()

        options.set_capability ("isHeadless", "true")
        options.set_capability ("platformName", "iOS")
        options.set_capability ("platformVersion", environ.get ("MOBILETEST_PLATFORM_IOS_VERSION"))
        options.set_capability ("udid", environ.get ("MOBILETEST_PLATFORM_IOS_ID"))
        options.set_capability ("deviceName", environ.get ("MOBILETEST_PLATFORM_IOS_NAME"))
        options.set_capability ("app", environ.get ("MOBILETEST_APPLICATION_IOS_PATH"))
        options.set_capability ("enablePerformanceLogging", "true")

        self.driver = webdriver.Remote (environ.get ("MOBILETEST_REMOTE_ADDRESS", "http://localhost:4723/wd/hub"), options = options)

        yield

        self.driver.quit ()
