import os
import pytest
import time
from utils.browser_config import browser_for_download 
from pages.login_page import LoginPage
from pages.immigration import Immigration
from pathlib import Path
import time
import logging
from utils.logger_config import get_logger
logger = logging.getLogger(__name__)
from utils.config_reader import ConfigReader


@pytest.fixture
def browser():
    driver, download_folder = browser_for_download()
    driver.implicitly_wait(10)
    yield driver, download_folder
    driver.quit()


@pytest.fixture
def logged_in_browser(browser):
    driver, download_folder = browser

    login_page = LoginPage(driver)
    login_page.enter_username(ConfigReader.get("credentials", "username"))
    login_page.enter_password(ConfigReader.get("credentials", "password"))
    login_page.click_login()

    immigration_page = Immigration(driver)
    yield immigration_page, download_folder


def test_downloadimmigrationdocument(logged_in_browser):
    immigration, DOWNLOAD_FOLDER = logged_in_browser

    immigration.click_myinfo()
    immigration.click_immigration()
    immigration.click_download_file()

    expected_file = DOWNLOAD_FOLDER / ConfigReader.get("testdata", "filename")

    timeout = 15
    while timeout > 0:
        if expected_file.exists():
            break
        time.sleep(1)
        timeout -= 1

    assert expected_file.exists(), "Downloaded file not found!"