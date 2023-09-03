from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def userandpass(browserlocal):
    username_input = browserlocal.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = browserlocal.find_element(By.CSS_SELECTOR, "input[name='password']")
    username_input.send_keys("alextest149")
    password_input.send_keys("14021402alex")
    login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
def Gotoprofile(browserlocal):
    print("profile clicked ")
    profile_button = browserlocal.find_element(By.XPATH, "//img[@crossorigin='anonymous']")
    profile_button.click()


browser = webdriver.Firefox()
browser.implicitly_wait(35)
browser.get("https://www.instagram.com/")
print("instegram loaded ......")
sleep(11)
userandpass(browser)
sleep(11)
Gotoprofile(browser)
sleep(10)
following_button=browser.find_element(By.PARTIAL_LINK_TEXT, "following")
following_button.click()
sleep(5)

html = browser.find_element(By.CLASS_NAME, "_aano")
for i in range(0,1,1):
    sleep(1)
    html.send_keys(Keys.PAGE_DOWN)

list_of_elements = browser.find_elements(By.XPATH,"//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
print(len(list_of_elements))
list_of_elements[0].click()


print("finish")