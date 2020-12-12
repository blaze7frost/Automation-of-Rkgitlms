from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://my.rkgitlms.in//mod/bigbluebuttonbn//view.php?id=28")
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('1900330310038')
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('Physics2$')

login = driver.find_element_by_xpath('//*[@id="loginbtn"]')
login.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="join_button_input"]'))
    )
finally:
    driver.quit()
