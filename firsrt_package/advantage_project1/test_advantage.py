from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

from advantage_project.home_page_POM import Home_Page
from advantage_project.laptops_category_page import Laptops_category
from advantage_project.speakers_category_page import Speakers_category
from advantage_project.mice_category_page import Mice_category
from advantage_project.tablets_category_page import Tablets_category
from advantage_project.shopping_cart_page import Shopping_cart
from advantage_project.product_page import Product_page
from advantage_project.headphones_category_page import Headphons_category
from advantage_project.order_payment_page import Order_payment
from selenium.webdriver import ActionChains
from advantage_project.order_payment_page import Order_payment
from advantage_project.create_account_page import Create_account
from advantage_project.my_orders_page import My_orders
from advantage_project.log_in_page import Log_in_page



class TestAdvantage(TestCase):
    def setUp(self):
        print("setup")
        service1 = Service(r"C:\Selenium\chromedriver.exe")

        self.driver = webdriver.Chrome(service=service1)

        self.driver.get("http://www.advantageonlineshopping.com/")

        self.driver.maximize_window()

        # In case an element is not found - define a 10 seconds timeout
        self.driver.implicitly_wait(10)



        self.home_page = Home_Page(self.driver)
        self.speakers_category=Speakers_category(self.driver)
        self.laptops_category=Laptops_category(self.driver)
        self.tablets_category=Tablets_category(self.driver)
        self.mice_category=Mice_category(self.driver)
        self.headphons_category = Headphons_category(self.driver)
        self.shopping_cart=Shopping_cart(self.driver)
        self.product_page=Product_page(self.driver)
        self.order_payment=Order_payment(self.driver)
        self.wait=WebDriverWait(self.driver,10)
        self.actionChains = ActionChains(self.driver)
        self.order_payment = Order_payment(self.driver)
        self.create_account = Create_account(self.driver)
        self.my_orders=My_orders(self.driver)
        self.log_in=Log_in_page(self.driver)
        # WebDriverWait(self.driver, 10)



    def test_web_1(self):
        self.home_page.choose_speakers()
        self.speakers_category.choose_bose_soundlink_bluethooth_speakerIII()
        self.speakers_category.add_quantity()
        self.speakers_category.add_to_cart()
        self.speakers_category.choose_advantage_logo()


        self.home_page.choose_laptops()
        self.laptops_category.choose_HP_Chromebook_14_G1_ENERGY_STAR()
        self.laptops_category.add_quantity()
        self.laptops_category.add_quantity()
        self.laptops_category.add_to_cart()
        self.laptops_category.choose_advantage_logo()

        num_of_product=self.home_page.num_products_in_cart()
        self.assertEqual(num_of_product[1].text,'5')

    def test_web_2(self):
        self.home_page.choose_tablets()
        self.tablets_category.choose_HP_PRO_TABLET_608_G1()
        self.tablets_category.add_quantity()
        self.tablets_category.change_color_to_grey()
        self.tablets_category.add_to_cart()
        self.tablets_category.choose_advantage_logo()
        self.home_page.choose_headphones()
        self.headphons_category.choose_LOGITECH_USB_HEADSET_H390()
        self.headphons_category.change_color_to_yellow()
        self.headphons_category.add_to_cart()
        self.headphons_category.choose_advantage_logo()
        self.home_page.choose_laptops()
        self.laptops_category.choose_HP_Chromebook_14_G1_ENERGY_STAR()
        self.laptops_category.add_quantity()
        self.laptops_category.add_quantity()
        self.laptops_category.add_to_cart()
        list0 = self.home_page.list_names()
        self.assertEqual(list0[0].text, "HP CHROMEBOOK 14 G1(ENERGY ...")
        self.assertEqual(list0[1].text, "LOGITECH USB HEADSET H390")
        self.assertEqual(list0[2].text, "HP PRO TABLET 608 G1")
        list1 = self.home_page.list_quantity_and_colors()
        self.assertEqual(list1[0].text, "QTY: 3")
        self.assertEqual(list1[1].text, "Color: BLACK")
        self.assertEqual(list1[2].text, "QTY: 1")
        self.assertEqual(list1[3].text, "Color: YELLOW")
        self.assertEqual(list1[4].text, "QTY: 2")
        self.assertEqual(list1[5].text, "Color: GRAY")
        list2 = self.home_page.list_prices()
        self.assertEqual(list2[0].text, "$899.97")
        self.assertEqual(list2[1].text, "$39.99")
        self.assertEqual(list2[2].text, "$958.00")

    def test_web_3(self):
        self.home_page.choose_tablets()
        self.tablets_category.choose_HP_ELITEPAD_1000_G2_TABLET()
        self.tablets_category.add_to_cart()
        self.tablets_category.choose_advantage_logo()

        self.home_page.choose_mice()
        self.mice_category.choose_HP_Z3600_WIRELESS_MOUSE()
        self.mice_category.add_to_cart()
        self.mice_category.choose_advantage_logo()

        # remove the first item
        x1=self.home_page.list_of_products_shopping_cart()[1]
        self.home_page.remove_first_item()
        self.assertNotIn(x1,self.home_page.list_of_products_shopping_cart())



    def test_web_4(self):
        self.home_page.choose_speakers()
        self.speakers_category.choose_bose_soundlink_bluethooth_speakerIII()
        self.speakers_category.add_to_cart()
        self.speakers_category.choose_advantage_logo()
        self.home_page.choose_shopping_cart()

        self.assertEqual("SHOPPING CART",self.shopping_cart.bar_shopping_cart().text)


    def test_web_5(self):

        """product from tablets"""
        self.home_page.choose_tablets()
        self.tablets_category.choose_HP_ELITEPAD_1000_G2_TABLET()
        self.tablets_category.add_quantity()
        self.tablets_category.add_quantity()

        price_1=self.product_page.price_product()
        price_without_sign1=price_1.text.replace("$","")
        price_without_sign1=price_without_sign1.replace(",", "")
        price_1_number=float(price_without_sign1)
        quantity_1_number=int(self.product_page.quantity_value())
        sum_price_1=price_1_number*quantity_1_number
        print("product 1: HP_ELITEPAD_1000_G2_TABLET")
        print("quantity1:", quantity_1_number)
        print("price per one1:", price_1_number)

        self.tablets_category.add_to_cart()
        self.tablets_category.choose_advantage_logo()




        """product from mice"""
        self.home_page.choose_mice()
        self.mice_category.choose_HP_Z3600_WIRELESS_MOUSE()
        self.mice_category.add_quantity()

        price_2 = self.product_page.price_product()
        price_without_sign2 = price_2.text.replace("$", "")
        price_2_number = float(price_without_sign2)
        quantity_2_number = int(self.product_page.quantity_value())
        sum_price_2 = price_2_number * quantity_2_number
        print("product 2: HP_Z3600_WIRELESS_MOUSE")
        print("quantity2:", quantity_2_number)
        print("price per one2:", price_2_number)


        self.mice_category.add_to_cart()
        self.mice_category.choose_advantage_logo()




        """product from laptops"""
        self.home_page.choose_laptops()
        self.laptops_category.choose_HP_Chromebook_14_G1_ENERGY_STAR()
        self.laptops_category.add_quantity()
        self.laptops_category.add_quantity()
        self.laptops_category.add_quantity()

        price_3 = self.product_page.price_product()
        price_without_sign3 = price_3.text.replace("$", "")
        price_without_sign3 = price_without_sign3.replace(",", "")
        price_3_number = float(price_without_sign3)
        quantity_3_number=int(self.product_page.quantity_value())
        sum_price_3 = price_3_number * quantity_3_number
        print("product 3: HP_Chromebook_14_G1_ENERGY_STAR")
        print("quantity3:", quantity_3_number)
        print("price per one3:", price_3_number)

        self.laptops_category.add_to_cart()
        self.laptops_category.choose_advantage_logo()

        # get in shopping cart page
        self.home_page.choose_shopping_cart()

        price_4=self.shopping_cart.total_price()
        price_without_sign4=price_4.text.replace("$", "")
        price_without_sign4=price_without_sign4.replace(",", "")
        total_price_number=float(price_without_sign4)
        total_price_number=round(total_price_number,2)
        total_sum_prices=sum_price_1+sum_price_2+sum_price_3
        total_sum_prices=round(total_sum_prices,2)
        self.assertEqual(total_price_number,total_sum_prices)

    def test_web_6(self):
        self.home_page.choose_headphones()
        self.headphons_category.choose_LOGITECH_USB_HEADSET_H390()

        self.headphons_category.add_quantity()
        self.headphons_category.add_quantity()
        self.headphons_category.add_to_cart()
        self.headphons_category.choose_advantage_logo()

        self.home_page.choose_mice()
        self.mice_category.choose_HP_Z8000_BLUETOOTH_MOUSE()
        self.mice_category.add_to_cart()
        self.mice_category.choose_advantage_logo()

        self.home_page.choose_shopping_cart()
        e = self.driver.find_element(By.CSS_SELECTOR,"td[colspan='5']")
        self.actionChains.move_to_element(e).perform()

        self.shopping_cart.wait_for_window_to_disappear()

        self.shopping_cart.edit_product()
        self.mice_category.add_quantity()
        self.mice_category.add_quantity()
        self.mice_category.add_to_cart()
        self.mice_category.choose_advantage_logo()
        self.home_page.choose_shopping_cart()


        self.shopping_cart.edit_second_product()

        self.headphons_category.remove_quantity()

        self.headphons_category.add_to_cart()
        self.headphons_category.choose_advantage_logo()

        self.home_page.choose_shopping_cart()

        self.assertEqual("3",self.shopping_cart.how_much_quantity_first().text)
        self.assertEqual("2",self.shopping_cart.how_much_quantity_second().text)

    def test_web_7(self):
        self.home_page.choose_tablets()

        self.tablets_category.choose_HP_PRO_TABLET_608_G1()

        self.driver.back()

        self.assertTrue("TABLETS", self.tablets_category.tablets_bar().text)
        self.driver.back()
        self.assertTrue("OUR PRODUCTS", self.home_page.home_page_check())

    def test_web_8(self):
        self.home_page.choose_mice()
        self.mice_category.choose_HP_Z3600_WIRELESS_MOUSE()
        self.mice_category.add_to_cart()
        self.mice_category.choose_advantage_logo()
        self.home_page.choose_laptops()
        self.laptops_category.choose_HP_PAVILION_15Z_LAPTOP()
        self.laptops_category.add_quantity()
        self.laptops_category.add_to_cart()
        self.laptops_category.choose_advantage_logo()
        self.home_page.choose_shopping_cart()
        self.shopping_cart.check_out_button()
        sleep(3)
        self.order_payment.select_registration()
        self.create_account.create_username()
        self.create_account.create_password()
        self.create_account.create_Email()
        self.create_account.confirm_password()
        self.create_account.agree_theme_of_service()
        sleep(2)
        self.create_account.register_confirm()

        self.order_payment.next_to_payment_method()
        sleep(2)
        self.order_payment.safe_pay_username()
        self.order_payment.safe_pay_passowrd()
        self.order_payment.pay_now()
        sleep(2)
        self.assertEqual(self.order_payment.oreder_finished().text, "Thank you for buying with Advantage")

        number_of_order = self.order_payment.number_order()
        self.home_page.choose_profile_button()
        self.home_page.my_orders()
        sleep(2)

        # print(number_of_order)
        # print(self.my_orders.list_orders_number())
        self.assertTrue(number_of_order in self.my_orders.list_orders_number())
        self.home_page.choose_shopping_cart()
        self.assertEqual(self.shopping_cart.empty_shopping_cart().text,"Your shopping cart is empty")

    def test_web_9(self):
        self.home_page.choose_speakers()
        self.speakers_category.choose_HP_S9500_BLUETOOTH_WIRELESS_SPEAKER()
        self.speakers_category.add_to_cart()
        self.speakers_category.choose_advantage_logo()
        self.home_page.choose_headphones()
        self.headphons_category.choose_LOGITECH_USB_HEADSET_H390()
        self.headphons_category.add_to_cart()
        self.headphons_category.choose_advantage_logo()
        self.laptops_category.choose_advantage_logo()
        self.home_page.choose_shopping_cart()
        self.shopping_cart.check_out_button()
        sleep(3)
        self.order_payment.username_login()
        self.order_payment.password_login()
        sleep(5)
        self.order_payment.login_button()
        sleep(3)
        self.order_payment.next_to_payment_method()
        self.order_payment.mastercard_option()
        sleep(3)
        self.order_payment.cvv_number()
        self.order_payment.card_number()
        self.order_payment.card_holder_name()
        self.order_payment.mm_Expiration_date()
        self.order_payment.yyyy_Expiration_date()
        sleep(3)
        # self.order_payment.dont_save_changes()
        sleep(3)
        self.order_payment.pay_now_master_card()
        sleep(7)

        number_of_order = self.order_payment.number_order()
        self.home_page.choose_profile_button()
        self.home_page.my_orders()
        sleep(2)
        self.assertTrue(number_of_order in self.my_orders.list_orders_number())


        self.home_page.choose_shopping_cart()
        self.assertEqual(self.shopping_cart.empty_shopping_cart().text, "Your shopping cart is empty")

    def test_web_10(self):
        self.home_page.choose_profile_button()
        self.log_in.enter_username()
        self.log_in.enter_password()

        self.log_in.choose_sign_in()
        sleep(3)
        self.assertEqual(self.home_page.check_account_name().text,"noa1234")

        self.home_page.choose_profile_button()

        self.home_page.sign_out()
        sleep(3)
        self.assertNotEqual(self.home_page.check_account_name().text,"noa1234")
        print(self.home_page.check_account_name())



















# if __name__ == '__main__':
#     unittest.main()
