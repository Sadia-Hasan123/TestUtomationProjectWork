import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

from pages.front_page import Front
from pages.login import LoginPage

class Login_test(unittest.TestCase):
    def test_login(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        fp = Front(driver)
        fp.front_page()

        lp = LoginPage(driver)
        lp.login_page("hasansadia940@gmail.com", "123456")
        time.sleep(3)

        driver.close()