import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
from pages.login import LoginPage
from pages.front_page import Front
from pages.T_shirt_page import T_ShirtPage
from pages.payment_page import PaymentPage


class Tshirt_SelectionTest(unittest.TestCase):
    def test_tshirt_selection(self):
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

        tp = T_ShirtPage(driver)
        tp.t_shirt_page()
        time.sleep(3)

        pp = PaymentPage(driver)
        pp.payment_page()
        time.sleep(3)


