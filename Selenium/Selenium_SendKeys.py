from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get('http://demostore.supersqa.com/my-account/')

u_name = driver.find_element('id', 'username')
u_name.send_keys('asdasd')
u_pass = driver.find_element('id', 'password')
u_pass.send_keys('asdasd')

submit = driver.find_element('css selector', '#customer_login > div.u-column1.col-1 > form > p:nth-child(3) > button').click()

search_field = driver.find_element('id', 'woocommerce-product-search-field-0')
search_field.send_keys('dupa')
time.sleep(3)
search_field.send_keys(Keys.ENTER)







