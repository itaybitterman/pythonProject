from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Mice_category:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_HP_Z3600_WIRELESS_MOUSE(self):
        self.driver.find_element(By.ID,"27").click()

    def choose_HP_Z8000_BLUETOOTH_MOUSE(self):
        self.driver.find_element(By.ID, "33").click()

    def add_quantity(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='plus']").click()

    def add_to_cart(self):
        self.driver.find_element(By.NAME,"save_to_cart").click()

    def advantage_logo(self):
        return self.driver.find_element(By.CSS_SELECTOR,".logoDemo")

    def choose_advantage_logo(self):
        self.advantage_logo().click()
