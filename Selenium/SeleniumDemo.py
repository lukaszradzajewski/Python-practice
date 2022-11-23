## all about driver: https://www.selenium.dev/documentation/en/webdriver/driver_requirements/

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# option 1 (Selenium 4)
# se = Service(executable_path='C:\\Users\48575\\Downloads\\chromedriver_win32\\chromedriver')
# driver = webdriver.Chrome(service=se)

# option 2 is adding the executable to system path

driver = webdriver.Chrome()
driver.get("http://www.google.com")
# here you should add the XPath of the 'I agree' button
item = driver. find_element(By.XPATH, value="/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]")

# Then we need to add an action to it. We want to click it, so we will use the following
item.click()

search = driver.find_element(By.NAME, value="q")
search.send_keys("Kitku" + Keys.ENTER)


