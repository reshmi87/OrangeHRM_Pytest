from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
from utils.logger_config import get_logger
from selenium.webdriver.common.keys import Keys
from utils.waits import wait_for_loader_to_disappear
logger = logging.getLogger(__name__)
from selenium.webdriver.common.by import By

class Dependants:
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

    def click_dependents(self):
        self.driver.find_element(By.LINK_TEXT,"Dependents").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Assigned Dependents']"))
        )
        logger.info("Dependents Page is loaded ")
    
    def click_add_dependents(self):
        self.driver.find_element(By.XPATH,"//h6[text()='Assigned Dependents']/../button").click()
        wait_for_loader_to_disappear(self.driver)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h6[text()='Add Dependent']"))
        )

    def enter_name(self,name):
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Name')]/../../div[2]/input").send_keys(name)

    def select_relationship(self):
        self.driver.find_element(By.XPATH,"//label[contains(text(),'Relationship')]/../../div[2]/div/div/div[2]").click() 
        self.driver.find_element(By.XPATH,"//span[contains(text(),'Child')]").click()

    def enter_dob(self,dob):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH,"//label[contains(text(),'Date of Birth')]/../../div[2]//input")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(dob)

    def save_dependent(self):
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
    
    def get_all_dependents(self):
        rows = self.driver.find_elements(
        By.XPATH, "//div[@class='oxd-table-body']/div/div")
        values = []
        for row in rows:
            cell_value = row.find_element(By.XPATH, ".//div[2]/div").text
            values.append(cell_value)
        logger.info(values)
        return values