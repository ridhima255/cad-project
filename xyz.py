from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import configparser

# Read username and password from config file
config = configparser.ConfigParser()
#create a config.conf file on Desktop
config.read("C:/Users/Ayush/OneDrive/Desktop/config.conf")

username = config.get('credentials', 'username')
password = config.get('credentials', 'password')

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.instagram.com/")

searchBox = driver.find_element(By.CSS_SELECTOR, "[name=username]")
searchBox.send_keys(username)
passwordBox = driver.find_element(By.CSS_SELECTOR, "[name=password]")
passwordBox.send_keys(password)

searchBox.send_keys(Keys.ENTER)

time.sleep(5)

driver.get("https://www.instagram.com/ibm?igsh=MW44M3o4b216MzIwbQ==")
time.sleep(7)

firstReel = driver.find_element(By.CSS_SELECTOR, 'a[href^="/reel/C6_0GYLx"]')
firstReel.click()

time.sleep(5)

audioToggleButton = driver.find_element(
    By.CSS_SELECTOR, 'button[aria-label="Toggle audio"]')
audioToggleButton.click()

time.sleep(2)

while True:
    try:
        nextButton = driver.find_element(By.CSS_SELECTOR, "_aaqg _aaqh")
        nextButton.click()
        time.sleep(20)
    except:
        break

time.sleep(20)
driver.quit()
