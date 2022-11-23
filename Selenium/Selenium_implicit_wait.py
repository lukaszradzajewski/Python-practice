from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.implicitly_wait(10)  # waits 10secs

driver.get('http://demostore.supersqa.com/')
try:
    userName = driver.find_element(By.ID, 'username')
    userName.click()
except Exception as e:
    print('element not found')
    driver.close()
    raise








