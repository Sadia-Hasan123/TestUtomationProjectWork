import time

from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class T_ShirtPage:
    def __init__(self, driver):
        self.driver = driver

    def t_shirt_page(self):
        t_shirtbtn = self.driver.find_element(By.XPATH, '//*[@id="block_top_menu"]/ul/li[3]/a')
        self.driver.implicitly_wait(3)
        t_shirtbtn.click()

        t_shirtTab = self.driver.find_element(By.XPATH, '//*[@id="center_column"]/ul/li/div')
        self.driver.implicitly_wait(3)
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(t_shirtTab).perform()
            time.sleep(4)

            color = self.driver.find_element(By.ID, 'color_2')
            color.click()
            time.sleep(2)


        except:
            print('Mouse Hover Action Failed2.')

        addToCart = self.driver.find_element(By.XPATH, '//*[@id="add_to_cart"]/button')
        self.driver.implicitly_wait(3)
        addToCart.click()
        time.sleep(4)

        message = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[1]/h2')
        time.sleep(2)

        display = message.is_displayed()
        if display is True:
            print('Add successfully')
        else:
            print('failed')

        time.sleep(2)
        proceed = self.driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a')
        proceed.click()
        time.sleep(2)