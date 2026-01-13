from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def username_input(self):
        return self.driver.find_element(By.NAME, "username")
    
    def password_input(self):
        return self.driver.find_element(By.NAME, "password")

    def login_button(self):
        return self.driver.find_element(By.XPATH, "//button[@type='submit']")
    
    def enter_username(self, username):
        self.username_input().send_keys(username)

    def enter_password(self, password):
        self.password_input().send_keys(password)

    def click_login(self):
        self.login_button().click()