from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Product_page:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def price_product(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"[class='roboto-thin screen768 ng-binding']")[0]

    def quantity_of_product(self):
        return self.driver.find_element(By.NAME,"quantity")

    def quantity_value(self):
        return self.quantity_of_product().get_attribute("value")









