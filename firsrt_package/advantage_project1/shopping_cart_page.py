from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class Shopping_cart:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def bar_shopping_cart(self):
        return self.driver.find_element(By.CSS_SELECTOR,"[class='select  ng-binding']")

    def total_price(self):
        list1=self.driver.find_elements(By.CSS_SELECTOR,"[class='roboto-medium ng-binding']")
        print("len list",len(list1))

        return self.driver.find_elements(By.CSS_SELECTOR,".cart-total")[0]

    def edit_product(self):
        Edit = self.driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")
        Edit[0].click()

    def edit_second_product(self):
        Edit = self.driver.find_elements(By.CSS_SELECTOR, "[class='edit ng-scope']")
        Edit[1].click()

    def how_much_quantity_first(self):
        quantity_first = self.driver.find_elements(By.CSS_SELECTOR, "tr[class='ng-scope']>td>[class='ng-binding']")
        return quantity_first[0]

    def how_much_quantity_second(self):
        quantity_second = self.driver.find_elements(By.CSS_SELECTOR, "tr[class='ng-scope']>td>[class='ng-binding']")
        return quantity_second[1]

    def check_out_button(self):
        self.driver.find_element(By.ID, "checkOutButton").click()

    def wait_for_window_to_disappear(self):
        self.wait.until(EC.invisibility_of_element_located((By.CSS_SELECTOR,"td[colspan='3']")))

    def empty_shopping_cart(self):
        return  self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-bold ng-scope']")