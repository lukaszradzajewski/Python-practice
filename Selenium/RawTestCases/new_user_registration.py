from selenium import webdriver
from selenium.webdriver.common.by import By
import string
import random
import time

driver = webdriver.Chrome()
driver.implicitly_wait(5)

url = 'http://demostore.supersqa.com/my-account/'
email_field_id = 'reg_email'
password_field_id = 'reg_password'
logout_btn_css = 'li.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout'
time.sleep(2)

# go to the url
driver.get(url)
email_field = driver.find_element(By.ID, email_field_id)

# generate random email
letters = string.ascii_lowercase
random_string = ''.join(random.choice(letters) for i in range(15))
random_email = random_string + '@supersqa.com'

# type in the email field
email_field.send_keys(random_email)

# find password field and enter password
password_field = driver.find_element(By.ID, password_field_id)
password_field.send_keys('mynewpassword123!')

time.sleep(2)

register_btn = driver.find_element(By.CSS_SELECTOR, 'button[value="Register"]')
register_btn.click()

logout_btn = driver.find_element(By.CSS_SELECTOR, logout_btn_css)

if logout_btn.is_displayed():
    print("PASS")
else:
    print("User not logged in")
