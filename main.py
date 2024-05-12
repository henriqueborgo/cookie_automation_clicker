#Importing libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException, TimeoutException
import threading
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
button_upgrade_prefix = "upgrade"
value_product_prefix = "productPrice"

#Thread to keep the big cookie clicking running in paralel
def click_big_cookie():
    while True:
        button_bigcookie.click()

click_thread = threading.Thread(target=click_big_cookie)
click_thread.start()

#Loop to buy products and upgrades
while True:
    #Buy products to increase productivity
    for i in range(11,-1,-1):     
        #Check the amount of cookies available
        value_cookie_count_raw = driver.find_element(By.ID,"cookies").text
        value_cookies_count = value_cookie_count_raw.split(" ")[0].replace(",","").split("\n")[0]
        #Check the value of the product price
        product_price_raw = driver.find_element(By.ID, value_product_prefix + str(i)).text
        #print("product_price_raw: ",product_price_raw)
        product_price = product_price_raw.replace(",","").replace(" million","").replace(" billion","")
        #print("product_price: ",product_price)
        #Check if product is already enabled
        if not product_price.isdigit():
            try:
                product_price = float(product_price)
            except ValueError:
                continue
        
        #Adjust the cookie count number
        if "million cookies" in value_cookie_count_raw:
            #print("value_cookie_count_raw: ",value_cookie_count_raw)
            #print("value_coolie_count: ",value_cookies_count)
            value_cookies_count = float(value_cookies_count)*1000000
            #print("Cookie Million adjusted: ", value_cookies_count)
        if "billion cookies" in value_cookie_count_raw:
            value_cookies_count = float(value_cookies_count)*1000000000
            #print("Cookie Billion: ", value_cookies_count)
        
        #Adjust the product price number
        if "million" in product_price_raw:
            product_price = float(product_price)*1000000
            #print("Price Million: ",product_price)
        if "billion" in product_price_raw:
            product_price = float(product_price)*1000000000
            #print("Price Billion: ",product_price)
        
        #Buy products if balance available
        if float(value_cookies_count) > float(product_price):
            #Wait until the product is located
            WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, button_product_prefix + str(i))))
            #Scroll the page to get the element visible
            product = driver.find_element(By.ID, button_product_prefix + str(i))
            driver.execute_script("arguments[0].scrollIntoView(true)", product)
            #Buy the product            
            product.click()
            break
    
    #Buy upgrades to increase productivity
    for j in range(2):
        #Check if the upgrade is available
        try:
            #Wait until the product to be present in the DOM of the page
            WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.ID, button_upgrade_prefix + str(j))))
            upgrade = driver.find_element(By.ID,button_upgrade_prefix + str(j))
            if upgrade.get_attribute("class") == "crate upgrade enabled":
                upgrade.click()
        except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException,TimeoutException):
            break