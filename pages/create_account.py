import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class CreateAccountPage:
    def __init__(self, driver):
        self.driver = driver

    def create_account(self, firstname, lastname, password, company, Address, city, Zip, addInfo, HPhone, Mphone,
                       refAddress):

        # select gender

        MrsRadioBtn = self.driver.find_element(By.ID, 'id_gender2')
        MrsRadioBtn_status = MrsRadioBtn.is_selected()
        if not MrsRadioBtn_status:
            MrsRadioBtn.click()
        time.sleep(2)

        firstname_field = self.driver.find_element(By.ID, 'customer_firstname')
        firstname_field.send_keys(firstname)

        lastname_field = self.driver.find_element(By.ID, 'customer_lastname')
        lastname_field.send_keys(lastname)

        password_field = self.driver.find_element(By.ID, 'passwd')
        password_field.send_keys(password)

        day_field = self.driver.find_element(By.ID, 'days')
        sel = Select(day_field)
        sel.select_by_value('11')

        month_field = self.driver.find_element(By.ID, 'months')
        sel = Select(month_field)
        sel.select_by_value('7')

        year_field = self.driver.find_element(By.ID, 'years')
        sel = Select(year_field)
        sel.select_by_value('1997')
        time.sleep(2)

        company_field = self.driver.find_element(By.ID, 'company')
        company_field.send_keys(company)

        address_field = self.driver.find_element(By.ID, 'address1')
        address_field.send_keys(Address)

        city_field = self.driver.find_element(By.ID, 'city')
        city_field.send_keys(city)

        state_field = self.driver.find_element(By.ID, 'id_state')
        sel2 = Select(state_field)
        sel2.select_by_value('5')
        time.sleep(2)

        zip_field = self.driver.find_element(By.ID, 'postcode')
        zip_field.send_keys(Zip)

        country_field = self.driver.find_element(By.ID, 'id_country')
        sel3 = Select(country_field)
        sel3.select_by_value('21')
        time.sleep(2)

        addInfo_field = self.driver.find_element(By.ID, 'other')
        addInfo_field.send_keys(addInfo)

        hPhone_field = self.driver.find_element(By.ID, 'phone')
        hPhone_field.send_keys(HPhone)

        mphone_field = self.driver.find_element(By.ID, 'phone_mobile')
        mphone_field.send_keys(Mphone)

        refadd_field = self.driver.find_element(By.ID, 'alias')
        refadd_field.send_keys(refAddress)
        time.sleep(3)

        register = self.driver.find_element(By.ID, 'submitAccount')
        register.click()
        time.sleep(2)
