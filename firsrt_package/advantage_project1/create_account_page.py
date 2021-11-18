from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Create_account:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def create_username(self):
        username = self.driver.find_element(By.NAME, "usernameRegisterPage")
        username.click()
        username.send_keys("skk0633")

    def create_password(self):
        password = self.driver.find_element(By.NAME, "passwordRegisterPage")
        password.click()
        password.send_keys("Shlomitay111")

    def create_Email(self):
        Email = self.driver.find_element(By.NAME, "emailRegisterPage")
        Email.click()
        Email.send_keys("hiworld41@gmail.com")

    def confirm_password(self):
        password = self.driver.find_element(By.NAME, "confirm_passwordRegisterPage")
        password.click()
        password.send_keys("Shlomitay111")

    def agree_theme_of_service(self):
        self.driver.find_element(By.NAME, "i_agree").click()

    def register_confirm(self):
        self.driver.find_element(By.ID, "register_btnundefined").click()
