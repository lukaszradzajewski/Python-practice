from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")

cart = driver.find_element(By.ID, "site-header-cart")
cart.click()

driver.get("http://demostore.supersqa.com/my-account/")
userName = driver.find_element(By.ID, 'username')
userName.send_keys('myusername')

