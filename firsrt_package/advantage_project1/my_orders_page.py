from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class My_orders:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def list_orders_number(self):
        order_numbers_elements= self.driver.find_elements(By.CSS_SELECTOR,"[class='ng-binding']")
        order_numbers=[]
        for i in order_numbers_elements:
            order_numbers.append(i.text)
        return order_numbers


