from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/checkbox_example.html')

# Example 1
# select_61_80 = driver.find_element('css selector', 'input[name="age-group-checkbox"][value="61-80"]')
# select_61_80.click()
#
# assert select_61_80.is_selected(), "After clicking chosen value it is not selected."

# Example 2
# Verify the number of checkboxes and if they are selectable


expectedNumberOfOptions = 4
allCheckboxes = driver.find_elements('name', 'age-group-checkbox')
assert len(allCheckboxes) == expectedNumberOfOptions, f'Number of checkboxes is different than {expectedNumberOfOptions}'


for checkbox in allCheckboxes:
    checkbox.click()
    value = checkbox.get_attribute('value')
    if checkbox.is_selected():
        print(f"Checkbox with value '{value}' is selectable")
    else:
        raise Exception(f"Value '{value}' is not selectable")

