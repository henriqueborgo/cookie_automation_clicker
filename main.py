#Importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#Downloading webdriver
#download it and paste the chromedriver.exe to the same folder as main.py
#https://sites.google.com/chromium.org/driver/

#Service and driver function
service = Service(execution_path="chrome_driver.exe")
driver = webdriver.Chrome(service=service)

#Open the cookie clicker game
driver.get("https://orteil.dashnet.org/cookieclicker/")

#Wait until the cookies settings opens
WebDriverWait(driver, 5). until(
    EC.presence_of_element_located((By.XPATH,"//p[@class='fc-button-label' and text()='Consent']"))
)

#Accept cookie button click
button_cookies_accept = driver.find_element(By.XPATH,"//p[@class='fc-button-label' and text()='Consent']")
button_cookies_accept.click()

#Wait until the language selector opens
WebDriverWait(driver, 5). until(
    EC.presence_of_element_located((By.ID,"langSelect-EN"))
)

#Select language
button_language_english = driver.find_element(By.ID, "langSelect-EN")
button_language_english.click()

#Wait until the game is loaded
time.sleep(5)

#Declaring variables
button_bigcookie = driver.find_element(By.ID,"bigCookie")
button_product_prefix = "product"
value_product_prefix = "productPrice"

#Creating a loop to click on the big cookie
while True:
    button_bigcookie.click()

    #Buy products to increase productivity
    for i in range(8):
        #Check the amount of cookies available
        value_cookies_count = driver.find_element(By.ID,"cookies").text.split(" ")[0]
        #Check the value of the product price
        product_price = driver.find_element(By.ID, value_product_prefix + str(i)).text.replace(",","")

        #Check if product is already enabled
        if not product_price.isdigit():
            try:
                product_price = int(product_price)
            except ValueError:
                break

        #Buy products if balance available
        if int(value_cookies_count) > int(product_price):
            product = driver.find_element(By.ID, button_product_prefix + str(i))
            product.click()
            break
    