import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login_page(self, email, password):
        email_field = self.driver.find_element(By.ID, 'email')
        email_field.clear()
        email_field.send_keys(email)

        password_field = self.driver.find_element(By.ID, 'passwd')
        password_field.clear()
        password_field.send_keys(password)

        signIn = self.driver.find_element(By.ID, 'SubmitLogin')
        signIn.click()
