import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.create_account import CreateAccountPage
from pages.front_page import Front
from pages.signupPage import SignUp


class CreateAccountTest(unittest.TestCase):
    def test_create_account(self):
        baseURL = "http://automationpractice.com/index.php"
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.maximize_window()
        driver.implicitly_wait(3)
        driver.get(baseURL)
        time.sleep(3)

        fp = Front(driver)
        fp.front_page()

        sp = SignUp(driver)
        sp.signup_page("hasansadia240@gmail.com")

        cp = CreateAccountPage(driver)
        cp.create_account("Sadia", "Hasan", "123456", "abcd", "cantonment", "Dhaka", "12345",
                          "iuwerioerijj", "89273983", "01837387834", "Dhaka")

        driver.close()
