from selenium import webdriver
from selenium.webdriver.support.ui import Select


driver = webdriver.Chrome()

driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/drop_down_example.html')

# option 1 is using the Select class
first_dropdown = driver.find_element('id', 'age-range-select')
first_dropdown_object = Select(first_dropdown)
first_dropdown_object.select_by_index(1)

# option 2
dropdown_button = driver.find_element('id', 'dropdownMenuButton')
dropdown_button.click()
second_dropdown = driver.find_element('xpath', '/html/body/div[2]/div[2]/div/ul/li[3]/a')
second_dropdown.click()

