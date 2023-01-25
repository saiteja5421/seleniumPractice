from selenium.webdriver.common.by import By
from pageObjects.conformPage import conformPage


class checkOutPage:
    def __init__(self, driver):
        self.driver = driver

    titles = (By.XPATH, "//div[@class='card h-100']")
    title_text = (By.TAG_NAME, "h4")
    add_button = (By.CSS_SELECTOR, "button[class='btn btn-info']")
    check_out = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")
    checkout=(By.CSS_SELECTOR,"button[class='btn btn-success']")

    def get_titles(self):
        return self.driver.find_elements(*checkOutPage.titles)

    def get_title_text(self, phone):
        return phone.find_element(*checkOutPage.title_text).text

    def click_add_button(self,phone):
        return phone.find_element(*checkOutPage.add_button).click()

    def check_out_button(self):
        return self.driver.find_element(*checkOutPage.check_out).click()

    def checkout_page(self):
        self.driver.find_element(*checkOutPage.checkout).click()
        conform_page=conformPage(self.driver)
        return conform_page
