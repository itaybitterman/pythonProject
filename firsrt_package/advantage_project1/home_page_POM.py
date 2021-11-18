from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Home_Page:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def choose_speakers(self):
        self.driver.find_element(By.ID, "speakersTxt").click()

    def choose_headphones(self):
        self.driver.find_element(By.ID,"headphonesTxt").click()

    def choose_tablets(self):
        self.driver.find_element(By.ID,"tabletsTxt").click()

    def choose_mice(self):
        self.driver.find_element(By.ID,"miceTxt").click()

    def choose_laptops(self):
        self.driver.find_element(By.ID, "laptopsTxt").click()

    def choose_profile_button(self):
        self.driver.find_element(By.ID,"menuUserSVGPath").click()

    def num_products_in_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='cart ng-binding']")


    def remove_first_item(self):
        x_button = self.driver.find_elements(By.CSS_SELECTOR, "[class='removeProduct iconCss iconX']")
        x_button[0].click()

    def wait_for_home_page_load (self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"[class='menu navLinks roboto-regular ng-scope']")))


    def choose_shopping_cart(self):
        self.driver.find_element(By.ID,"menuCart").click()


    def list_of_products_shopping_cart(self):
        return self.driver.find_elements(By.CSS_SELECTOR,"tr[id=product]>td>a>h3.ng-binding")

    def home_page_check(self):
        self.driver.find_element(By.CSS_SELECTOR, "[class='menu navLinks roboto-regular ng-scope']")

    def list_quantity_and_colors(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "a>label.ng-binding")

    def list_prices(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[class='price roboto-regular ng-binding']")

    def list_names(self):
        list1 = self.driver.find_elements(By.CSS_SELECTOR, "a>h3.ng-binding")
        print("len", len(list1))
        for i in list1:
            print("text", i.text)

        return list1

    def my_orders(self):
        self.driver.find_elements(By.CSS_SELECTOR, "label[translate='My_Orders']")[1].click()

    def sign_out(self):
        self.driver.find_elements(By.CSS_SELECTOR,"[class='option roboto-medium ng-scope']")[2].click()

    def check_account_name(self):
        return self.driver.find_elements(By.CSS_SELECTOR, "[data-ng-show='userCookie.response']")[1]


