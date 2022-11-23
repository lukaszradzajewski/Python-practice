from selenium import webdriver

driver = webdriver.Chrome()

driver.get('file:///C:/Users/48575/Desktop/Python/Selenium/Multiple_windows_and_tabs/windows-and_tabs_example.html')
driver.find_element('xpath', '//*[@id="windows"]/a[1]').click()

all_window_handles = driver.window_handles
oryginal_window = all_window_handles[0]
print('Before switching window focus: ' + driver.title)
new_window = all_window_handles[1]

driver.switch_to.window(new_window)
print('After switching window focus: ' + driver.title)
print('Closing tab')
driver.close()
print('Switching to original window')
driver.switch_to.window(oryginal_window)
print('Original window: ' + driver.title)
