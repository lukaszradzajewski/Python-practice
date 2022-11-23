from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/iFrames_example.html')
# example without iFrame
# driver.find_element(By.ID, 'btnOutFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just Clicked Outside iFrame', 'Something went wrong'
# my_alert.accept()

# example with iFrame
# my_frame = driver.find_element(By.ID, 'myFrame1')
# driver.switch_to.frame(my_frame)
# driver.find_element(By.ID, 'btnInFrame').click()
# my_alert = driver.switch_to.alert
# my_alert_text = my_alert.text
# assert my_alert_text == 'Just Clicked Inside iFrame', 'Something went wrong'
# my_alert.accept()
# driver.switch_to.default_content()
# driver.find_element(By.ID, 'btnOutFrame').click()

# example with iFrame using 'ID'
# driver.switch_to.frame('myFrame1')
# driver.find_element(By.ID, 'btnInFrame').click()
# print(driver.switch_to.alert.text)
# driver.switch_to.alert.dismiss()

# example with iFrame using 'index', 0 - first iFrame found, 1 - another/nested iFrame etc.
driver.switch_to.frame(0)
driver.find_element(By.ID, 'btnInFrame').click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.dismiss()
