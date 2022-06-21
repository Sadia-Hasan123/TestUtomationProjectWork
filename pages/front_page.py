import time
from selenium.webdriver.common.by import By


class Front:
    def __init__(self, driver):
        self.driver = driver

    def front_page(self):
        # Click sign in button
        signInBtn = self.driver.find_element(By.LINK_TEXT, 'Sign in')
        signInBtn.click()
        time.sleep(2)


