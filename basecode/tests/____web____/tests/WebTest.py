from ..src.TestCase import TestCase
from selenium.webdriver.common.by import By

class WebTest (TestCase):

    def test_web (self) -> None:
        """
        :rtype: None
        """
        self.driver.get ("http://localhost:80")

        element = self.driver.find_element (By.TAG_NAME, "div").find_element (By.XPATH, "h1")

        self.assertEqual (element.text, "Configuration")
