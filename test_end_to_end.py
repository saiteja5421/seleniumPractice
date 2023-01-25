from logging import getLogger

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pageObjects.Homepage import HomePage
from pageObjects.checkOutPage import checkOutPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BaseClass import BaseClass
from conftest import setup


class TestEnd(BaseClass):

    def test_end(self):
        log=self.getLogger()
        homepage = HomePage(self.driver)
        check_out_page= homepage.click_shop_button()
        phones = check_out_page.get_titles()
        phone_titles = []
        for phone in phones:
            # phoneTitles.append(check_out_page.get_title_text().text)
            # print(phone.find_element(By.TAG_NAME,"h4").text)
            phone_titles.append(check_out_page.get_title_text(phone))
            # phoneTitles.append(title)
            check_out_page.click_add_button(phone)
        # add_buttons = driver.find_elements(By.CSS_SELECTOR, "button[class='btn btn-info']")
        print(phone_titles)
        check_out_page.check_out_button()
        # element=check_out_page.check_out_button()
        # element.get_attribute()
        conform_page = check_out_page.checkout_page()
        # print(element)
        # self.driver.find_element(By.ID,"country").send_keys("ind")
        conform_page.search_element().send_keys("ind")

        # wait=WebDriverWait(self.driver,5)
        # wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
        self.verifyLinkPresence("India")

        log.info("India is clicked")
        conform_page.click_country().click()
        conform_page.click_checkbox().click()
        conform_page.click_purchase().click()
        text = conform_page.get_success_text().text

        assert ("Success! Thank you!" in text)