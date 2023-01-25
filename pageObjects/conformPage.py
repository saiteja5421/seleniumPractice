from selenium.webdriver.common.by import By


class conformPage:
    def __init__(self,driver):
        self.driver=driver

    search=(By.ID, "country")
    present_country=(By.LINK_TEXT,"India")
    checkbox=By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']"
    purchase=(By.CSS_SELECTOR,"input[class='btn btn-success btn-lg']")
    text=By.CSS_SELECTOR,"div[class='alert alert-success alert-dismissible']"

    def search_element(self):
        return self.driver.find_element(*conformPage.search)

    def click_country(self):
        return self.driver.find_element(*conformPage.present_country)

    def click_checkbox(self):
        return self.driver.find_element(*conformPage.checkbox)

    def click_purchase(self):
        return self.driver.find_element(*conformPage.purchase)

    def get_success_text(self):
        return self.driver.find_element(*conformPage.text)


