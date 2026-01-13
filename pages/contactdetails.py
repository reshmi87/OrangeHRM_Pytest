from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from selenium.webdriver.common.keys import Keys
from utils.waits import wait_for_loader_to_disappear
from utils.logger_config import get_logger
logger = logging.getLogger(__name__)

class ContactDetails:
    def __init__(self, driver):
        self.driver = driver
    
    def click_myinfo(self):
        self.driver.find_element(By.LINK_TEXT, "My Info").click()
        logger.info("Clicked My Info")
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.NAME, "firstName"))
        )
        logger.info("My Info page loaded ")

    def click_contact_details(self):
        self.driver.find_element(By.LINK_TEXT,"Contact Details").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[contains(text(),'Street 1')]"))
        )
        logger.info("Contact Details Page loaded ")
    
    def enter_street1(self,street1):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Street 1')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(street1)
        
    def enter_city(self,city):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'City')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(city)

    def enter_state(self,state):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'State/Province')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(state)

    def enter_zip(self,zip):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Zip/Postal Code')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(zip)
       
    def click_country(self):
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Country')]/../../div[2]//i").click()

    def select_country(self):
        self.driver.find_element(By.XPATH,"//span[contains(text(),'United States')]").click()
    
    def enter_homephone(self,homeno):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Home')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(homeno)
        

    def enter_mobilephone(self,mobileno):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Mobile')]/../../div[2]/input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(mobileno)
        
    def save_contact(self):
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
    
    def check_street(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH, "//label[contains(text(),'Street 1')]/../../div[2]/input")))
        return element.get_attribute("value")
    
    def check_mobile(self):
        element = WebDriverWait(self.driver, 10).until(
        EC.visibility_of_element_located(
            (By.XPATH,"//label[contains(text(),'Mobile')]/../../div[2]/input")))
        return element.get_attribute("value")