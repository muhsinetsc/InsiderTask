from selenium.webdriver.common.by import By

BASE_URL = "https://useinsider.com/"

CLICK_ACCEPT_ALL_BUTTON = (By.ID,"wt-cli-accept-all-btn")
CLICK_COMPANY_BUTTON = (By.CSS_SELECTOR,"li:nth-of-type(6) > a#navbarDropdownMenuLink")
CLICK_CAREERS_BUTTON = (By.CSS_SELECTOR,".new-menu-dropdown-layout-6-mid-container a:nth-of-type(2)")