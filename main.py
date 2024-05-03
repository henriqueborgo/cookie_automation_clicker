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