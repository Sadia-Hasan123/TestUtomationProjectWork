import time
from selenium.webdriver.common.by import By


class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def signup_page(self, email):
        # Input into email field

        email_field = self.driver.find_element(By.ID, 'email_create')
        email_field.send_keys(email)

        # create account button click

        CrtAccBtn = self.driver.find_element(By.ID, 'SubmitCreate')
        CrtAccBtn.click()
        time.sleep(2)