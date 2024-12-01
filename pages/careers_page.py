import pytest
from pages.base_page import *
from constants.careers_page_locator import *

@pytest.mark.usefixtures("setup")
class CareersPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def hover_see_all_teams(self):
        self.hover_over_element(SEE_ALL_TEAMS)

    def click_see_all_teams(self):
        self.click_to_element(SEE_ALL_TEAMS)
        
    def product_design_wait(self):
        self.hover_over_element(PRODUCT_DESIGN_WAIT)

    def hover_our_locations_block(self):
        self.hover_over_element(OUR_LOCATIONS_BLOCK)

    def hover_life_at_insider_block(self):
        self.hover_over_element(LIFE_AT_INSIDER_BLOCK)

    

