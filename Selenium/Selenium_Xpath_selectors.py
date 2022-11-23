"""
// relative xpath
/ absolute xpath

//tag[@attribute='value']
//*[@attribute='value']
"""
# cart
#  //*[@id="site-header-cart"]
# //ul[@id="site-header-cart"]'
# /html/body/div/header/div[2]/div/ul
# '//ul[contains(@id, "site")]'
# '//a[text()="Lost your password?"]'
# '//a[contains(text(), "password?")]'

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://demostore.supersqa.com")
cart = driver.find_element(By.XPATH, '//ul[@id="site-header-cart"]')
cart.click()