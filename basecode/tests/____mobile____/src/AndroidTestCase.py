import unittest
import pytest
from abc import ABC
from os import environ
from appium import webdriver
from appium.options.android import UiAutomator2Options

class AndroidTestCase (ABC, unittest.TestCase):

    @pytest.fixture
    def setup_and_teardown (self) -> None:
        """
        :rtype: None
        """
        options = UiAutomator2Options ()

        options.set_capability ("isHeadless", "true")
        options.set_capability ("platformName", "Android")
        options.set_capability ("platformVersion", environ.get ("MOBILETEST_PLATFORM_ANDROID_VERSION"))
        options.set_capability ("udid", environ.get ("MOBILETEST_PLATFORM_ANDROID_ID"))
        options.set_capability ("deviceName", environ.get ("MOBILETEST_PLATFORM_ANDROID_NAME"))
        options.set_capability ("app", environ.get ("MOBILETEST_APPLICATION_ANDROID_PATH"))
        options.set_capability ("enablePerformanceLogging", "true")

        self.driver = webdriver.Remote (environ.get ("MOBILETEST_REMOTE_ADDRESS", "http://localhost:4723/wd/hub"), options = options)

        yield

        self.driver.quit ()
