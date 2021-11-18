from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep


service1=Service(r"C:\Selenium\chromedriver.exe")

driver=webdriver.Chrome(service=service1)


driver.get("https://www.advantageonlineshopping.com/#/")
driver.maximize_window()

# in case an element is not found - define a 10 seconds timeout
driver.implicitly_wait(10)
wait = WebDriverWait(driver,10)

# headphones_category=driver.find_element(By.ID,"headphonesTxt")
# headphones_category.click()
# sleep(2)
# driver.back()
#
# speakers_category=driver.find_element(By.ID,"speakersTxt")
# speakers_category.click()
# sleep(2)
# driver.back()
#
#
# tablets_category=driver.find_element(By.ID,"tabletsTxt")
# tablets_category.click()
# sleep(2)
# driver.back()
#
#
# mice_category=driver.find_element(By.ID,"miceTxt")
# mice_category.click()
# sleep(2)
# driver.back()
#
#
# laptops_category=driver.find_element(By.ID,"laptopsTxt")
# laptops_category.click()
# sleep(2)
# driver.back()
# ==============================================================================================
# profile=driver.find_element(By.ID,"menuUserSVGPath")
# profile.click()
#
# Username=driver.find_element(By.NAME,"username")
# Username.send_keys("itay1234")
#
# Password=driver.find_element(By.NAME,"password")
# Password.send_keys("Itay1234")
#
# sign_in=driver.find_element(By.ID,"sign_in_btnundefined")
# sign_in.click()
#
# speakers_category=driver.find_element(By.ID,"speakersTxt")
# speakers_category.click()
# sleep(3)
#
# bose_soundlink_bluethooth_speakerIII= driver.find_element(By.ID,"20")
# bose_soundlink_bluethooth_speakerIII.click()
#
# add_quantity=driver.find_element(By.CSS_SELECTOR,"[class='plus']")
# add_quantity.click()
#
# add_to_cart=driver.find_element(By.NAME,"save_to_cart")
# add_to_cart.click()
#
#
# sleep(3)
#
# Advantage_logo=driver.find_element(By.CSS_SELECTOR,".logoDemo")
# Advantage_logo.click()
#
#
# laptops_category=driver.find_element(By.ID,"laptopsTxt")
# laptops_category.click()
#
# HP_Chromebook_14_G1_ENERGY_STAR=driver.find_element(By.ID,"9")
# HP_Chromebook_14_G1_ENERGY_STAR.click()
#
# add_quantity=driver.find_element(By.CSS_SELECTOR,"[class='plus']")
# add_quantity.click()
# add_quantity.click()
#
# add_to_cart=driver.find_element(By.NAME,"save_to_cart")
# add_to_cart.click()
#
# Advantage_logo=driver.find_element(By.CSS_SELECTOR,".logoDemo")
# Advantage_logo.click()
#
# sleep(6)
#
# num_products=driver.find_elements(By.CSS_SELECTOR,"[class='cart ng-binding']")
# if num_products[1].text=='5':
#     print("test pass")
# else:
#     print("test faild")

# ==========================================================================================

# laptops_category=driver.find_element(By.ID,"laptopsTxt")
# laptops_category.click()
# HP_PAVILION_15Z_LAPTOP=driver.find_element(By.ID,"3")
# HP_PAVILION_15Z_LAPTOP.click()
# add_to_cart=driver.find_element(By.NAME,"save_to_cart")
# add_to_cart.click()
# Advantage_logo=driver.find_element(By.CSS_SELECTOR,".logoDemo")
# Advantage_logo.click()
#
#
mice_category=driver.find_element(By.ID,"miceTxt")
mice_category.click()
HP_Z3600_WIRELESS_MOUSE=driver.find_element(By.ID,"27")
HP_Z3600_WIRELESS_MOUSE.click()
add_to_cart=driver.find_element(By.NAME,"save_to_cart")
add_to_cart.click()
Advantage_logo=driver.find_element(By.CSS_SELECTOR,".logoDemo")
Advantage_logo.click()


tablets_category=driver.find_element(By.ID,"tabletsTxt")
tablets_category.click()
HP_PRO_TABLET_608_G1=driver.find_element(By.ID,"18")
HP_PRO_TABLET_608_G1.click()
add_quantity=driver.find_element(By.CSS_SELECTOR,"[class='plus']")
add_quantity.click()
add_to_cart=driver.find_element(By.NAME,"save_to_cart")
add_to_cart.click()
Advantage_logo=driver.find_element(By.CSS_SELECTOR,".logoDemo")
Advantage_logo.click()

# x_button=driver.find_elements(By.CSS_SELECTOR,"[class='removeProduct iconCss iconX']")
# x_button[0].click()
#
choose_shopping_cart=driver.find_element(By.ID,"menuCart")
choose_shopping_cart.click()

# sleep(4)
# list_products_shopping_cart=driver.find_elements(By.CSS_SELECTOR,"tr[id=product]>td>a>h3.ng-binding")
# list_products_shopping_cart[0].click()
sleep(3)
# shopping_cart_button=driver.find_element(By.CSS_SELECTOR,"[class='select  ng-binding']")
sleep(3)













