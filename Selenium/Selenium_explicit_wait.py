from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

driver.get('http://demostore.supersqa.com/')

userName = wait.until(EC.visibility_of_all_elements_located((By.ID, 'username')))

userName.click()









