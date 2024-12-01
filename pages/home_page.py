import pytest
from pages.base_page import *
from constants.home_page_locator import *

@pytest.mark.usefixtures("setup")
class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_accept_all_button(self):
        self.click_to_element(CLICK_ACCEPT_ALL_BUTTON)

    def click_company_button(self):
        self.click_to_element(CLICK_COMPANY_BUTTON)
        
        
    def click_careers_button(self):
        self.click_to_element(CLICK_CAREERS_BUTTON)
    
        