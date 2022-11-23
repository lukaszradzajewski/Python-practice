from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class InvalidUserLoginError:
    invalid_email = 'abc@supersqa.com'
    url = 'http://demostore.supersqa.com/my-account/'
    expected_msg = 'Error: The password you entered for the email address abc@supersqa.com is incorrect. Lost your password?'

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        time.sleep(2)

    def go_to_my_account(self):
        self.driver.get(self.url)

    def input_email(self):
        username_field = self.driver.find_element(By.ID, 'username')
        username_field.send_keys(self.invalid_email)

    def input_pass(self):
        password_field = self.driver.find_element(By.ID, 'password')
        password_field.send_keys('abcdefge')

    def click_login(self):
        self.driver.find_element(By.NAME, 'login').click()

    def verify_error_message(self):
        error_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/ul/li')
        displayed_error = error_element.text
        assert displayed_error == self.expected_msg, "Displayed message of error is not matching expected text."
        print("PASS")

    def main(self):
        self.go_to_my_account()
        self.input_email()
        self.input_pass()
        time.sleep(2)
        self.click_login()
        self.verify_error_message()
        self.driver.quit()


if __name__ == '__main__':
    obj = InvalidUserLoginError()
    obj.main()
