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


def Gotopost(conter1):
    list_of_elements = browser.find_elements(By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
    print("Eleman select new")
    list_of_elements[conter1].click()


def pageDown():
    html = browser.find_element(By.CLASS_NAME, "_aano")
    html.send_keys(Keys.PAGE_DOWN)


def Hezarfollow(adadlocal):
    dot = adadlocal.find('.')
    adad = int(adadlocal[0:dot])
    adadlow = int(adadlocal[dot + 1])
    adad = (adad * 1000) + (adadlow * 100)
    return adad


def followerandfollowing():
    global follower1
    elements = browser.find_elements(By.XPATH, "//span[@class='_ac2a']")
    if ('K' in elements[1].text):
        follower1 = Hezarfollow(elements[1].text)
        print(follower1)

    elif ('M' in elements[1].text):
        dot = elements[1].text.find('.')
        print(elements[1].text[0:dot])
    elif (',' in elements[1].text):
        ashar = int(elements[1].text.find(','))
        adadbig = int(elements[1].text[0:ashar])
        follower1 = (adadbig * 1000) + int(elements[1].text[ashar + 1: len(elements[1].text)])
        print(follower1)
    else:
        follower1 = int(elements[1].text)
        print(follower1)

    if (',' in elements[2].text):
        ashar = int(elements[2].text.find(','))
        adadbig = int(elements[2].text[0:ashar])
        following = (adadbig * 1000) + int(elements[2].text[ashar + 1: len(elements[2].text)] * 100)
        print(following)
    else:
        following = int(elements[2].text)
        print(following)

    return follower1, following


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
sleep(10)

html = browser.find_element(By.CLASS_NAME, "_aano")
list_of_elements = browser.find_elements(By.XPATH, "//span[@class='_aacl _aaco _aacw _aacx _aad7 _aade']")
conter = 0
flag = 0
while conter < (len(list_of_elements)):

    Gotopost(conter1=flag)
    sleep(3)
    follower, following = followerandfollowing()
    follow_back = browser.find_element(By.XPATH, "//div[@class='_aacl _aaco _aacw _aad6 _aade']")
    print(follow_back.text)
    if (follow_back.text == 'Follow' or follow_back.text == 'Follow Back'):
        exit(0)
    minfollow = (follower - following)
    if (minfollow > 900):
        butten_follower = browser.find_element(By.XPATH, "//button[@class='_acan _acap _acat _aj1-']")
        butten_follower.click()
        sleep(3)
        butten_unfollw = browser.find_elements(By.XPATH,
                                               "//div[@class='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1pi30zi x1swvt13 x1l90r2v xyamay9 x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1']")
        butten_unfollw[4].click()

    else:
        flag += 1
    sleep(4)
    browser.back()
    sleep(4)
    conter += 1
    if (conter % 5 == 0):
        pageDown()
        sleep(5)
print("finish")
