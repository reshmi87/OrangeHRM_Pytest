import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from utils.browser_config import launch_browser
from pages.login_page import LoginPage
from pages.personaldetails import PersonalDetails
from pages.contactdetails import ContactDetails
from pages.dependents import Dependants
from pages.immigration import Immigration
from pathlib import Path
import os
import time
import logging
from utils.logger_config import get_logger

logger = logging.getLogger(__name__)

@pytest.fixture
def browser():
    driver = launch_browser()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_browser(browser):
    login_page = LoginPage(browser)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()
    return browser

def test_login_page(logged_in_browser):
    assert "OrangeHRM" in logged_in_browser.title
    logging.info("Login Successful")

def test_firstname_lastname(logged_in_browser):
    personaldetails = PersonalDetails(logged_in_browser)
    personaldetails.click_myinfo()
    personaldetails.enter_firstname("Peter")
    personaldetails.enter_lastname("Thomson")
    personaldetails.save_names()
    profilename = personaldetails.profile_name()
    logger.info("Profilename: %s", profilename)
    assert profilename == "Peter Thomson"

def test_contact_details(logged_in_browser):
    contactdetails = ContactDetails(logged_in_browser)
    contactdetails.click_myinfo()
    contactdetails.click_contact_details()
    contactdetails.enter_street1("251 penn avenue")
    contactdetails.enter_city("Austin")
    contactdetails.enter_state("Texas")
    contactdetails.enter_zip("76856")
    contactdetails.click_country()
    contactdetails.select_country()
    contactdetails.enter_homephone("678965567")
    contactdetails.enter_mobilephone("9878908765")
    contactdetails.save_contact()
    street= contactdetails.check_street()
    logger.info("Street Name: %s", street)
    assert street == "251 penn avenue"
    mobile= contactdetails.check_mobile()
    logger.info("Mobile Number: %s",mobile)
    assert mobile == "9878908765"

def test_dependents(logged_in_browser):
    dependents = Dependants(logged_in_browser)
    dependents.click_myinfo()
    dependents.click_dependents()
    # For Dependent1   
    dependents.click_add_dependents()
    dependents.enter_name("AChild1")
    dependents.select_relationship()
    dependents.enter_dob("2011-08-08")
    dependents.save_dependent()
     # For Dependent2
    dependents.click_dependents()
    dependents.click_add_dependents()
    dependents.enter_name("AChild2")
    dependents.select_relationship()
    dependents.enter_dob("2020-01-01")
    dependents.save_dependent()
    dependents.click_dependents()
    listofdependents = dependents.get_all_dependents()
    assert "AChild1" in listofdependents
    assert "AChild2" in listofdependents 

def test_immigration(logged_in_browser):
    immigration = Immigration(logged_in_browser)
    immigration.click_myinfo()
    immigration.click_immigration()
    immigration.add_immigration()
    immigration.add_number("P12432")
    immigration.add_issued_date("2020-01-01")
    immigration.add_expiry_date("2030-01-01")
    immigration.add_eligibility("Valid")
    immigration.select_issued_country()
    immigration.save_immigration()
    immigration.click_immigration()
    immigration_list = immigration.get_all_immigration()
    assert "P12432" in immigration_list

def test_addimmigrationdocument(logged_in_browser):
    immigration = Immigration(logged_in_browser)
    immigration.click_myinfo()
    immigration.click_immigration() 
    immigration.click_addattachments()
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    file_path = PROJECT_ROOT / "test_data" / "upload_files" / "Passport_test.txt"
    immigration.enter_file_path(file_path)
    immigration.save_upload_file()
    immigration.click_immigration()
    immigration_files_list = immigration.get_allfiles
    assert "Passport_test.txt" in immigration_files_list()