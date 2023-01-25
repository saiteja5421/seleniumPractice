import time

import pytest
from selenium.webdriver.common.by import By

from BaseClass import BaseClass
from selenium import webdriver

from pageObjects.Homepage import HomePage


class TestPage(BaseClass):

    def test_home(self, getData):
        log = self.getLogger()
        home_page=HomePage(self.driver)
        home_page.typing_name().send_keys(getData['firstname'])
        log.info("typed name : sai teja")
        home_page.typing_email().send_keys(getData['email'])
        home_page.typing_password().send_keys(getData
                                              ['password'])

        self.selectOptionByText(home_page.select_gender(), 'Male')
        home_page.click_employ_type().click()
        home_page.bday_date().send_keys(10121998)
        home_page.click_submit_button().click()
        success_text=home_page.get_success_text().text
        print(success_text)
        assert 'Success!' in success_text

    @pytest.fixture(params=[{'firstname':'saiteja','email':'saiteja@gmail.com','password':'sai'},
                            {'firstname':'saiteja','email':'saiteja@gmail.com','password':'sai'},
                            {'firstname':'saiteja','email':'saiteja@gmail.com','password':'sai'}])
    def getData(self,request):
        return request.param

