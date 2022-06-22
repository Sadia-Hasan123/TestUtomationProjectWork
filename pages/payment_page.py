import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


class PaymentPage:
    def __init__(self, driver):
        self.driver = driver

    def payment_page(self):
        checkout = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/p[2]/a[1]')
        self.driver.implicitly_wait(3)
        checkout.click()
        time.sleep(2)

        checkout2 = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/form/p/button')
        self.driver.implicitly_wait(3)
        checkout2.click()
        time.sleep(2)

        checkbox = self.driver.find_element(By.ID, 'cgv')
        checkbox_status = checkbox.is_selected()
        if not checkbox_status:
            checkbox.click()
        time.sleep(2)

        checkout3 = self.driver.find_element(By.XPATH, '//*[@id="form"]/p/button')
        self.driver.implicitly_wait(3)
        checkout3.click()

        pay_by_check = self.driver.find_element(By.XPATH, '//*[@id="HOOK_PAYMENT"]/div[2]/div/p/a')
        self.driver.implicitly_wait(3)
        pay_by_check.click()

        confirm = self.driver.find_element(By.XPATH, '//*[@id="cart_navigation"]/button')
        self.driver.implicitly_wait(3)
        confirm.click()

        sign_out = self.driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div/div/nav/div[2]/a')
        self.driver.implicitly_wait(3)
        sign_out.click()
