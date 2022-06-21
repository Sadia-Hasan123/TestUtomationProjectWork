import time
from selenium.webdriver.common.by import By


class Front:
    def __init__(self, driver):
        self.driver = driver

    def front_page(self, email):
        # Click sign in button
        signInBtn = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        signInBtn.click()
        time.sleep(2)

        # Input into email field

        email_field = self.driver.find_element(By.ID, 'email_create')
        email_field.send_keys(email)

        # create account button click

        CrtAccBtn = self.driver.find_element(By.ID, 'SubmitCreate')
        CrtAccBtn.click()
        time.sleep(2)
