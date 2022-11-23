from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/radios_example.html')

value = '21-40'
locator_by_value = f'input[name="age-group-radio"][value="{value}"]'

expected_default_value = '21-40'

# Example 1. verify if default is selected

default_element = driver.find_element(By.CSS_SELECTOR, locator_by_value.format(value=expected_default_value))
assert default_element.is_selected(), f"The default value of {expected_default_value} is not selected."

# Example 2.

expected_values = ['21-40', '41-60', '61-80', '81+']
all_radiobuttons = driver.find_elements(By.CSS_SELECTOR, 'input[name="age-group-radio"]')
assert len(all_radiobuttons) == len(expected_values), "the number of radiobuttons does not match the expected number"
