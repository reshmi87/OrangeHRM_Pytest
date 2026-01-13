from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
from utils.config_reader import ConfigReader


def launch_browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.get(ConfigReader.get("app", "url"))
    return driver

def browser_for_download():
    
    PROJECT_ROOT = Path(__file__).resolve().parent.parent
    DOWNLOAD_FOLDER = PROJECT_ROOT / "test_data" / "download_files"
    DOWNLOAD_FOLDER.mkdir(parents=True, exist_ok=True)
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": str(DOWNLOAD_FOLDER),  
        "download.prompt_for_download": False,               
        "directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    driver.maximize_window()
    driver.get(ConfigReader.get("app", "url"))
    return driver, DOWNLOAD_FOLDER

