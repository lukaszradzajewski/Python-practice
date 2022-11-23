from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/alerts_example.html')

# example1 - JS alert

alert_JS = driver.find_element(By.CSS_SELECTOR, 'div#jsAlertExample button')
alert_JS.click()

my_alert = driver.switch_to.alert

assert my_alert.text == 'I am a JavaScript Alert', 'Unexpected text on alert.'
sleep(2)
my_alert.accept()
# my_alert.dismiss()

# example2 - 'confirm' alert

alert_Confirm = driver.find_element(By.CSS_SELECTOR, 'div#jsConfirmExample button')
alert_Confirm.click()

my_alert = driver.switch_to.alert
sleep(2)
my_alert.accept()
confirm_message = driver.find_element(By.ID, 'userResponse1').text

assert confirm_message == 'Great! You will love it!', 'Wrong message after accepting'

# example3 - 'prompt' alert

alert_prompt = driver.find_element(By.CSS_SELECTOR, 'div#jsPromptExample button')
alert_prompt.click()
my_alert = driver.switch_to.alert
sleep(2)
my_alert.send_keys('Dupa dupa dupa')
my_alert.accept()
prompt_message = driver.find_element(By.ID, 'userResponse2').text

assert prompt_message == 'You have entered: Dupa dupa dupa', 'Cos nie pyklo...'
