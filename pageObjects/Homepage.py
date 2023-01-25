from selenium.webdriver.common.by import By
from pageObjects.checkOutPage import checkOutPage


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shopButton = (By.LINK_TEXT, "Shop")
    name = (By.NAME, "name")
    email = By.NAME, "email"
    password = (By.ID, "exampleInputPassword1")
    gender = (By.ID, "exampleFormControlSelect1")
    employ_type = (By.ID, 'inlineRadio1')

    bday = (By.NAME, 'bday')
    submit=(By.CSS_SELECTOR, "input[class='btn btn-success']")
    success=(By.CLASS_NAME,"alert-success")

    def click_shop_button(self):
        self.driver.find_element(*HomePage.shopButton).click()
        check_out_page = checkOutPage(self.driver)
        return check_out_page

    def typing_name(self):
        return self.driver.find_element(*HomePage.name)

    def typing_email(self):
        return self.driver.find_element(*HomePage.email)

    def typing_password(self):
        return self.driver.find_element(*HomePage.password)

    def select_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def click_employ_type(self):
        return self.driver.find_element(*HomePage.employ_type)

    def bday_date(self):
        return self.driver.find_element(*HomePage.bday)

    def click_submit_button(self):
        return self.driver.find_element(*HomePage.submit)

    def get_success_text(self):
        return self.driver.find_element(*HomePage.success)

