import pytest
from pages.base_page import *
from constants.job_page_locator import *

@pytest.mark.usefixtures("setup")
class JobPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def get_new_window(self):
        self.switch_to_new_window(1)