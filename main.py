from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


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


def Gotopost():
    list_of_elements = browser.find_elements(By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
    print("Eleman select new")
    list_of_elements[conter].click()


def pageDown():
    html = browser.find_element(By.CLASS_NAME, "_aano")
    html.send_keys(Keys.PAGE_DOWN)

def Hezarfollow(adadlocal):
    dot = adadlocal.find('.')
    adad = int(adadlocal[0:dot])
    adadlow = int(adadlocal[dot + 1])
    adad = (adad * 1000) + (adadlow * 100)
    return adad

browser = webdriver.Firefox()
browser.implicitly_wait(35)
browser.get("https://www.instagram.com/")
print("instegram loaded ......")
sleep(7)
userandpass(browser)
sleep(11)
Gotoprofile(browser)
sleep(10)
following_button = browser.find_element(By.PARTIAL_LINK_TEXT, "following")
following_button.click()
sleep(7)

html = browser.find_element(By.CLASS_NAME, "_aano")
list_of_elements = browser.find_elements(By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
conter = 0
while conter < (len(list_of_elements) - 30):
    for i in range(0, 4, 1):
        Gotopost()
        sleep(3)
        elements = browser.find_elements(By.XPATH, "//span[@class='_ac2a']")
        if('K' in elements[1].text ):
            follower=Hezarfollow(elements[1].text)
            print(follower)
            if('K' in elements[2].text):
                following=Hezarfollow(elements[2].text)
                print(following)
            else:
                following=int(elements[2].text)
        elif('M' in elements[1].text):
            dot = elements[1].text.find('.')
            print(elements[1].text[0:dot])


        sleep(3)
        browser.back()
        sleep(3)
        conter += 1
    pageDown()

print("finish")
