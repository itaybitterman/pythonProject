from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Log_in_page:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def username_field(self):
        return self.driver.find_element(By.NAME,"username")

    def enter_username(self):
        self.username_field().send_keys("noa1234")

    def password_field(self):
        return self.driver.find_element(By.NAME,"password")

    def enter_password(self):
        self.password_field().send_keys("Noa1234")

    def choose_sign_in(self):
        self.driver.find_element(By.ID,"sign_in_btnundefined").click()





