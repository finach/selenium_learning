from unittest import TestCase

import selenium.webdriver.support.ui
from mock import MagicMock
from mock import call
from mock import patch

from helper.helper_browser_controller import BrowserController


class TestBrowserController:
    @classmethod
    def setUpClass(cls):
        with patch("helper.helper_browser_controller.BrowserController") as mock_browser_controller:
            cls.mock_browser_controller = mock_browser_controller

    def test_buttonClick(self):
        with patch("selenium.webdriver.support.ui.WebDriverWait") as mock_WebDriverWait:
            xpath = 'button xpath'
            mock_WebDriverWait.return_value =
            self.mock_browser_controller.buttonClick(xpath)
            # mock_WebDriverWait.until.assert_called_once()
            # mock_WebDriverWait.until.click.assert_called_once()
            mock_WebDriverWait.assert_called()
