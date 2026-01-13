from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger_config import get_logger
from selenium.webdriver.common.keys import Keys
from utils.waits import wait_for_loader_to_disappear
logger = logging.getLogger(__name__)

class PersonalDetails:
    def __init__(self, driver):
        self.driver = driver
    
    def my_info(self):
        return self.driver.find_element(By.LINK_TEXT,"My Info")

    def firstname(self):
        return self.driver.find_element(By.XPATH, "//input[@name = 'firstName']")
    
    def lastname(self):
        return self.driver.find_element(By.XPATH, "//input[@name = 'lastName']")
    
    def savenames(self):
        return self.driver.find_element(By.XPATH,"//button[@type='submit']")
    
    def profilename(self):
        return self.driver.find_element(By.XPATH,"//div[@class='orangehrm-edit-employee-name']/h6")

    def click_myinfo(self):
        self.my_info().click()
        logger.info("Clicked My Info, waiting for First Name field")

    
    def enter_firstname(self,firstname):
        logger.info("Waiting for loader before interacting with First Name")
        wait_for_loader_to_disappear(self.driver)
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "firstName")))
        logger.info("Clearing existing First Name")
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        logger.info(f"Entering First Name: {firstname}")
        field.send_keys(firstname)
    
    def enter_lastname(self,lastname):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "lastName")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(lastname)
        submit = WebDriverWait(self.driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        return submit
   
    def save_names(self):
        logger.info("Waiting for form loader to disappear")
        WebDriverWait(self.driver, 20).until(
        EC.invisibility_of_element_located(
            (By.CLASS_NAME, "oxd-form-loader")))
        logger.info("Form loader gone, waiting for Save button to be clickable")
        save_button = WebDriverWait(self.driver, 20).until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[@type='submit']")))
        logger.info("Clicking Save button")
        save_button.click()

    def click_personal_details(self):
        logger.info("Waiting for form loader to disappear")
        self.driver.find_element(By.LINK_TEXT,"Personal Details").click()
        wait_for_loader_to_disappear(self.driver)
        logger.info("Personal Details Page loaded ")

    def profile_name(self):
        logger.info("Waiting for form loader to disappear")
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//div[@class='orangehrm-edit-employee-name']/h6")))
        return element.text
