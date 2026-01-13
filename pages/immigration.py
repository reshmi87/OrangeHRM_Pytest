from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger_config import get_logger
from selenium.webdriver.common.keys import Keys
from utils.waits import wait_for_loader_to_disappear
logger = logging.getLogger(__name__)
from selenium.webdriver.common.by import By

class Immigration:
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
    
    def click_immigration(self):
        self.driver.find_element(By.LINK_TEXT,"Immigration").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Assigned Immigration Records']"))
        )
        logger.info("Immigration page loaded ")
    
    def add_immigration(self):
        self.driver.find_element(By.XPATH,"//h6[text()='Assigned Immigration Records']/../button").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//label[text()='Document']")))
        
    def add_number(self,number):
        self.driver.find_element(By.XPATH,"//label[text()='Number']/../../div[2]/input").send_keys(number)
    
    def add_issued_date(self,date):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[text()='Issued Date']/../../div[2]//input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(date)

    def add_expiry_date(self,date):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[text()='Expiry Date']/../../div[2]//input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(date)
    
    def add_eligibility(self,status):
        self.driver.find_element(By.XPATH,"//label[text()='Eligible Status']/../../div[2]/input").send_keys(status)
    
    def select_issued_country(self):
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Issued By')]/../../div[2]/div/div/div[2]").click() 
        self.driver.find_element(By.XPATH,"//span[contains(text(),'India')]").click()
    
    def save_immigration(self):
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
    
    def get_all_immigration(self):
        rows = self.driver.find_elements(
        By.XPATH, "//div[@class='oxd-table-body']/div/div")
        values = []
        for row in rows:
            cell_value = row.find_element(By.XPATH, ".//div[3]/div").text
            values.append(cell_value)
        logger.info(values)
        return values
    
    def click_addattachments(self):
        self.driver.find_element(By.XPATH,"//h6[text()='Attachments']/../button").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH,"//label[contains(text(),'Select File')]")))
    
    def enter_file_path(self,path):
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Select File')]/../../div[2]/input").send_keys(str(path))
    
    def save_upload_file(self):
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
    
    def get_allfiles(self):
        rows = self.driver.find_elements(
        By.XPATH, "(//div[@class='oxd-table-body'])[2]/div/div")
        values = []
        for row in rows:
            cell_value = row.find_element(By.XPATH, ".//div[2]/div").text
            values.append(cell_value)
        logger.info(values)
        return values
    
    def click_download_file(self):
        self.driver.find_element(By.XPATH,"//div[contains(text(),'Passport_test.txt')]/../../div[8]//button[3]").click()
        