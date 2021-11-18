from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Order_payment:
    def __init__(self, driver: webdriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def select_registration(self):
        self.driver.find_element(By.ID,"registration_btnundefined").click()

    def next_to_payment_method(self):
        self.driver.find_element(By.ID,"next_btn").click()

    def safe_pay_username(self):
        username=self.driver.find_element (By.NAME,"safepay_username")
        username.click()
        username.send_keys("shlomitay422")

    def safe_pay_passowrd(self):
        password = self.driver.find_element(By.NAME, "safepay_password")
        password.click()
        password.send_keys("Shlomitay22")

    def pay_now(self):
        self.driver.find_element(By.ID,"pay_now_btn_SAFEPAY").click()

    def pay_now_master_card(self):
        self.driver.find_element(By.ID,"pay_now_btn_ManualPayment").click()

    def oreder_finished(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-regular ng-scope']")

    def no_order_exist(self):
        return self.driver.find_element(By.CSS_SELECTOR, "[class='roboto-bold ng-binding']")


    def number_order(self):
        # return self.driver.find_element(By.ID,"orderNumberLabel")
        self.wait.until(EC.visibility_of_element_located((By.ID,"orderNumberLabel")))
        return self.driver.find_element(By.ID,"orderNumberLabel").text


    def username_login(self):
        username_login = self.driver.find_element(By.NAME, "usernameInOrderPayment")
        username_login.click()
        username_login.send_keys("noa1234")

    def password_login(self):
        password_login = self.driver.find_element(By.NAME, "passwordInOrderPayment")
        password_login.click()
        password_login.send_keys("Noa1234")

    def login_button(self):
        self.driver.find_element(By.ID,"login_btnundefined").click()

    def mastercard_option(self):
        self.driver.find_element(By.NAME, "masterCredit").click()


    def card_number(self):
        card_number = self.driver.find_element(By.ID, "creditCard")
        card_number.click()
        card_number.send_keys("345424524524")

    def cvv_number(self):
        cvv_number = self.driver.find_element(By.NAME, "cvv_number")
        cvv_number.click()
        cvv_number.send_keys("678")

    def card_holder_name(self):
        card_holder_name = self.driver.find_element(By.NAME, "cardholder_name")
        card_holder_name.click()
        card_holder_name.send_keys("omerMalka")

    def mm_Expiration_date(self):
        mm=self.driver.find_element(By.NAME,"mmListbox")
        mm_drop_down=Select(mm)

        mm_drop_down.select_by_index(4)

    def yyyy_Expiration_date(self):
        yyyy=self.driver.find_element(By.NAME,"yyyyListbox")
        yyyy_drop_down=Select(yyyy)

        yyyy_drop_down.select_by_index(2)

    def dont_save_changes(self):
        self.driver.find_element(By.NAME,"save_master_credit").click()







