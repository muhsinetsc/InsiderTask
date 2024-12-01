import pytest
import time
from pages.base_page import BasePage
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.quality_assurance_page import QualityAssurancePage
from pages.job_page import JobPage
from constants.home_page_locator import *
from constants.careers_page_locator import *
from constants.quality_assurance_page_locator import *
from constants.job_page_locator import *


@pytest.mark.usefixtures("setup")
class TestInsider:

    def test_insider(self):
        base = BasePage(self.driver)
        home = HomePage(self.driver)
        careers = CareersPage(self.driver)
        quality_assurance = QualityAssurancePage(self.driver)
        job = JobPage(self.driver)


        # Çerezler kabul edilir.
        home.click_accept_all_button()

        # Ana sayfanın açıldığı doğrulanır.
        assert self.driver.current_url == "https://useinsider.com/", f"Expected 'https://useinsider.com/', but found '{self.driver.current_url}'"
        base.screenshot("screenshot/home_page.png")
    
        # "Company" menüsünün görüntülendiği doğrulanır ve "Company" butonuna tıklanır.
        assert (company_button := base.wait_for_element_to_be_visible(CLICK_COMPANY_BUTTON)).text == "Company", f"Expected: 'Company', but found: '{company_button.text}'"
        home.click_company_button()

        # "Careers" butonunun görüntülendiği doğrulanır ve "Careers" butonuna tıklanır.
        assert (careers_button := base.wait_for_element_to_be_visible(CLICK_CAREERS_BUTTON)).text == "Careers", f"Expected: 'Careers', but found: '{careers_button.text}'"
        home.click_careers_button()

        # "Careers" sayfasının açıldığı doğrulanır.
        assert self.driver.current_url == "https://useinsider.com/careers/", f"Expected 'https://useinsider.com/careers/', but found '{self.driver.current_url}'"
        base.screenshot("screenshot/careers_page.png")


        # "See All Teams" butonunun görüntülendiği doğrulanır ve "See All Teams" butonuna tıklanır.
        careers.hover_see_all_teams()
        assert (life_at_insider_block := base.wait_for_element_to_be_visible(SEE_ALL_TEAMS)).text == "See all teams", f"Expected: 'See all teams', but found: {life_at_insider_block}'"
        careers.click_see_all_teams()

        # Teams bloklarınnın görüntülendiği doğrulanır.
        careers.product_design_wait()
        assert len(teams_block := base.wait_for_elements_to_be_visible(TEAMS_BLOCK)) == 15, f"Expected 15 team blocks, but found {len(teams_block)}"
        

        # "Our Locations" bloğuna gidilir ve bloğun görüntülendiği doğrulanır.
        careers.hover_our_locations_block()
        assert (our_locations_block := base.wait_for_element_to_be_visible(OUR_LOCATIONS_BLOCK)).text == "Our Locations", f"Expected: 'Our Locations', but found: {our_locations_block}"
        
    
        # "Life at Insider" bloğuna gidilir ve bloğun görüntülendiği doğrulanır.
        careers.hover_life_at_insider_block()
        assert (life_at_insider_block := base.wait_for_element_to_be_visible(LIFE_AT_INSIDER_BLOCK)).text == "Life at Insider", f"Expected: 'Life at Insider', but found: {life_at_insider_block}'"
        


        # "https://useinsider.com/careers/quality-assurance/" linkinin yeni pencerede açıldığı doğrulanır.
        quality_assurance.new_url("https://useinsider.com/careers/quality-assurance/")
        assert self.driver.current_url == "https://useinsider.com/careers/quality-assurance/", f"Expected 'https://useinsider.com/careers/quality-assurance/', but found '{self.driver.current_url}'"
        base.screenshot("screenshot/new_url_page.png")


        # "See All QA Jobs" butonunun görüntülendiği doğrulanır ve "See All QA Jobs" butonuna tıklanır.
        assert (see_all_qa_jobs := base.wait_for_element_to_be_visible(SEE_ALL_QA_JOBS)).text == "See all QA jobs", f"Expected: 'See all QA jobs', but found: {see_all_qa_jobs}"
        quality_assurance.click_see_all_qa_jobs()

        # "Insider Open Positions | Insider" başlıklı sayfasının görüntülendiği doğrulanır.
        assert (positions_page_title := self.driver.title) == "Insider Open Positions | Insider", f"Expected title: 'Insider Open Positions | Insider', but found: '{positions_page_title}'"
        

        # "Quality Assurance" seçeneğinin görüntülenmesi beklenir.
        quality_assurance.wait_quality_asusurance()

        # "Quality Assurance" seçeneğinin görüntülendiği doğrulanır.
        assert (quality_assurance_title := base.wait_for_element_to_be_visible(QUALITY_ASSURANCE_TITLE)).get_attribute("title") == "Quality Assurance", f"Expected title: 'Quality Assurance', but found: '{quality_assurance_title.get_attribute('title')}'"
        

        # Lokasyonda "Istanbul, Turkey" seçeneğine tıklanır ve "Istanbul, Turkey" seçeneğinin görüntülendiği doğrulanır.
        quality_assurance.click_filter_by_location()
        quality_assurance.click_istanbul_turkey()
        assert (istanbul_turkey_title := base.wait_for_element_to_be_visible(ISTANBUL_TURKEY_TITLE)).get_attribute("title") == "Istanbul, Turkey", f"Expected title: 'Istanbul, Turkey', but found: '{istanbul_turkey_title.get_attribute('title')}'"
        

        # LOkasyon ve Departman isimleri doğrulanır.
        quality_assurance.hover_job()
        assert (location := base.wait_for_element_to_be_visible(LOCATION)).text == "Istanbul, Turkey", f"Istanbul, Turkey', but found: {location}"
        assert (department := base.wait_for_element_to_be_visible(DEPARTMENT)).text == "Quality Assurance", f"Quality Assurance', but found: {department}"
        base.screenshot("screenshot/job_page.png")

        # "View Role" beklenir ve butona tıklanır.
        base.wait_view_role_button()
        quality_assurance.click_view_role_button()
        

        # Başvuru sayfasının açıldığı doğrulanır.
        job.get_new_window()
        assert "jobs.lever.co/useinsider" in self.driver.current_url, f"Expected 'jobs.lever.co/useinsider' to be in '{self.driver.current_url}'"
        base.screenshot("screenshot/aplication_page.png")