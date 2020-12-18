from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import time
import pyautogui


PATH = "C:\\Program Files (x86)\\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://my.rkgitlms.in//mod/bigbluebuttonbn//view.php?id=28") #last page of the website where you have to join
username = driver.find_element_by_xpath('//*[@id="username"]')
username.send_keys('') #write your username
password = driver.find_element_by_xpath('//*[@id="password"]')
password.send_keys('') #write your password

login = driver.find_element_by_xpath('//*[@id="loginbtn"]')
login.click()

try:
    # for i in range(6):
    #     time.sleep(2)
    #     driver.refresh()            
    login = driver.find_element_by_xpath('//*[@id="join_button_input"]')
    login.click()
    time.sleep(30)
    pyautogui.press('tab') 
    pyautogui.press('tab') 
    pyautogui.press('tab') 
    pyautogui.press('enter') 
#     you can write yo rollnumber as well just write it and press enter 
    # mic = driver.find_element_by_class_name("//*[@id="tippy-123"]/span[1]")
    # mic.click()
    # mic1 = driver.find_element_by_class_name("//*[@id="tippy-22"]/span[1]/i")
    # mic1.click()
    # #   element = WebDriverWait(driver, 10).until(
    # #     EC.presence_of_element_located((By.XPATH, '//*[@id="join_button_input"]'))
    # #   )
    #     # time.sleep(2)
    #     # if i==5://*[@id="chat-messages"]/div[8]/div/div[2]/div[2]/p
    #     //*[@id="chat-messages"]/div[9]/div/div[2]/div[2]/p
    #     #     driver.quit()
    # https://s3.rkgit-meet.com/html5client/join?sessionToken=xhmdoxqbeeflu260 (data)

except:    
    driver.quit()
