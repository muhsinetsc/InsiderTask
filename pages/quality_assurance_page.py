import pytest
from pages.base_page import *
from constants.quality_assurance_page_locator import *

@pytest.mark.usefixtures("setup")
class QualityAssurancePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def new_url(self, url):
        self.navigate_to_url(url)

    def click_see_all_qa_jobs(self):
        self.click_to_element(SEE_ALL_QA_JOBS)

    def wait_quality_asusurance(self):
        self.wait_for_element_presence(WAIT_QUALITY_ASSURANCE)

    def click_filter_by_location(self):
        self.click_to_element(CLICK_FILTER_BY_LOCATION)

    def click_istanbul_turkey(self):
        self.click_to_element(CLICK_ISTANBUL_TURKEY)

    def wait_view_button(self):
        self.wait_for_element_presence(VIEW_ROLE_BUTTON)

    def click_view_role_button(self):
        self.get_element_index(0,VIEW_ROLE_BUTTON)
        self.hover_over_element_click(VIEW_ROLE_BUTTON)

    def hover_job(self):
        self.hover_over_element(LOCATION)
        time.sleep(2)
        
    

    