from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.waits import wait_for_loader_to_disappear

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
    def enter_username(self, username):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "username")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(username)

    def enter_password(self, password):
        field = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.NAME, "password")))
        field.click()
        field.send_keys(Keys.CONTROL, "a")
        field.send_keys(Keys.DELETE)
        field.send_keys(password)

    def click_login(self):
        self.login_button().click()