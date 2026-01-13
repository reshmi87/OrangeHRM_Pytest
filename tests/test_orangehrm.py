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
from utils.config_reader import ConfigReader

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
    login_page.enter_username(ConfigReader.get("credentials", "username"))
    login_page.enter_password(ConfigReader.get("credentials", "password"))
    login_page.click_login()
    return browser

def test_login_page(logged_in_browser):
    assert "OrangeHRM" in logged_in_browser.title
    logging.info("Login Successful")

def test_firstname_lastname(logged_in_browser):
    personaldetails = PersonalDetails(logged_in_browser)
    personaldetails.click_myinfo()
    personaldetails.enter_firstname(ConfigReader.get("testdata", "firstname"))
    personaldetails.enter_lastname(ConfigReader.get("testdata", "lastname"))
    personaldetails.save_names()
    personaldetails.click_personal_details()
    profilename = personaldetails.profile_name()
    logger.info("Profilename: %s", profilename)
    expected_name = (
    ConfigReader.get("testdata", "firstname") + " " +
    ConfigReader.get("testdata", "lastname"))
    assert profilename == expected_name

def test_contact_details(logged_in_browser):
    contactdetails = ContactDetails(logged_in_browser)
    contactdetails.click_myinfo()
    contactdetails.click_contact_details()
    contactdetails.enter_street1(ConfigReader.get("testdata", "street1"))
    contactdetails.enter_city(ConfigReader.get("testdata", "city"))
    contactdetails.enter_state(ConfigReader.get("testdata", "state"))
    contactdetails.enter_zip(ConfigReader.get("testdata", "zip"))
    contactdetails.click_country()
    contactdetails.select_country()
    contactdetails.enter_homephone(ConfigReader.get("testdata", "homephone"))
    contactdetails.enter_mobilephone(ConfigReader.get("testdata", "mobile"))
    contactdetails.save_contact()
    street= contactdetails.check_street()
    logger.info("Street Name: %s", street)
    assert street == ConfigReader.get("testdata", "street1")
    mobile= contactdetails.check_mobile()
    logger.info("Mobile Number: %s",mobile)
    assert mobile == ConfigReader.get("testdata", "mobile")

def test_dependents(logged_in_browser):
    dependents = Dependants(logged_in_browser)
    dependents.click_myinfo()
    dependents.click_dependents()
    # For Dependent1   
    dependents.click_add_dependents()
    dependents.enter_name(ConfigReader.get("testdata", "child1"))
    dependents.select_relationship()
    dependents.enter_dob(ConfigReader.get("testdata", "child1dob"))
    dependents.save_dependent()
     # For Dependent2
    dependents.click_dependents()
    dependents.click_add_dependents()
    dependents.enter_name(ConfigReader.get("testdata", "child2"))
    dependents.select_relationship()
    dependents.enter_dob(ConfigReader.get("testdata", "child2dob"))
    dependents.save_dependent()
    dependents.click_dependents()
    listofdependents = dependents.get_all_dependents()
    assert ConfigReader.get("testdata", "child1") in listofdependents
    assert ConfigReader.get("testdata", "child1") in listofdependents 

def test_immigration(logged_in_browser):
    immigration = Immigration(logged_in_browser)
    immigration.click_myinfo()
    immigration.click_immigration()
    immigration.add_immigration()
    immigration.add_number(ConfigReader.get("testdata", "number"))
    immigration.add_issued_date(ConfigReader.get("testdata", "issueddate"))
    immigration.add_expiry_date(ConfigReader.get("testdata", "expirydate"))
    immigration.add_eligibility(ConfigReader.get("testdata", "eligibility"))
    immigration.select_issued_country()
    immigration.save_immigration()
    immigration.click_immigration()
    immigration_list = immigration.get_all_immigration()
    assert ConfigReader.get("testdata", "number") in immigration_list

def test_addimmigrationdocument(logged_in_browser):
    immigration = Immigration(logged_in_browser)
    immigration.click_myinfo()
    immigration.click_immigration() 
    immigration.click_addattachments()
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    file_path = PROJECT_ROOT / "test_data" / "upload_files" / ConfigReader.get("testdata", "filename")
    immigration.enter_file_path(file_path)
    immigration.save_upload_file()
    immigration.click_immigration()
    immigration_files_list = immigration.get_allfiles
    assert ConfigReader.get("testdata", "filename") in immigration_files_list()