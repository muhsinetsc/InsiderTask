import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def screenshot(self, file_path):
        self.driver.save_screenshot(file_path)

    def wait_for_element_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
    
    def wait_for_elements_to_be_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
    
    def wait_for_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    
    def wait_view_role_button(self):
        time.sleep(2)

    def click_to_element(self, locator):
        self.wait_for_element_to_be_visible(locator).click()

    def hover_over_element(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_for_element_to_be_visible(locator)).perform()

    def hover_over_element_click(self, locator):
        ActionChains(self.driver).move_to_element(self.wait_for_element_to_be_visible(locator)).click().perform()

    def get_element_index(self, index, locator):
        self.wait_for_elements_to_be_visible(locator)[index]

    def navigate_to_url(self, url):
        self.driver.get(url)

    def switch_to_new_window(self,page):
        self.driver.switch_to.window(self.driver.window_handles[page])