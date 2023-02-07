from selenium import webdriver
import time
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import maskpass

user = "selenium.testing@abv.bg"
password = "pamporovo2023"
inpt_text = input("Text for the post: ")
driver = webdriver.Chrome()


def open_facebook():
    driver.maximize_window()
    driver.get('https://www.facebook.com/')
    print("Opened facebook")
    sleep(1)


def login(usr, pwd):
    accept_cookies = driver.find_element(By.XPATH, "//button[contains(string(), 'Allow essential and optional cookies')]")
    accept_cookies.click()
    username_box = driver.find_element(By.ID, 'email')
    username_box.send_keys(usr)
    print("Email Id entered")
    sleep(1)
    password_box = driver.find_element(By.ID, 'pass')
    password_box.send_keys(pwd)
    print("Password entered")
    login_box = driver.find_element(By.NAME, 'login')
    login_box.click()
    sleep(5)
    driver.get('https://www.facebook.com/')
    sleep(2)


def post_text(text):
    whats_on_your_mind_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div[3]/div/div[2]/div/div/div/div[1]/div/div[1]/span")
    whats_on_your_mind_field.click()
    sleep(2)
    post_field = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div[1]/div/div/div[1]")
    post_field.send_keys(text)
    sleep(2)
    post_button = driver.find_element(By.XPATH, "/html/body/div[1]/div[1]/div[1]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div/div/div[3]/div[2]/div/div/div[1]/div/span/span")
    post_button.click()


open_facebook()
login(user, password)
post_text(inpt_text)

print("Done")
input('Press anything to quit')
driver.quit()
print("Finished")
