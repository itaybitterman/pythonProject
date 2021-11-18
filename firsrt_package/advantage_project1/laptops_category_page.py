from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Laptops_category:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_HP_Chromebook_14_G1_ENERGY_STAR(self):
        self.driver.find_element(By.ID,"9").click()

    def choose_HP_PAVILION_15Z_LAPTOP(self):
        self.driver.find_element(By.ID, "2").click()

    def add_quantity(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='plus']").click()

    def add_to_cart(self):
        self.driver.find_element(By.NAME, "save_to_cart").click()

    def advantage_logo(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".logoDemo")

    def choose_advantage_logo(self):
        self.advantage_logo().click()