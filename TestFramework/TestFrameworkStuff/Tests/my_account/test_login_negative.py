import pytest
from TestFramework.TestFrameworkStuff.src.pages.MyAccountSignedOut import MyAccountSignedOut


@pytest.mark.usefixtures("init_driver")
class TestLoginNegative:

    @pytest.mark.tcid_1
    def test_login_none_existing_user(self):
        print("******")
        print("TEST LOGIN NON EXISTING")
        print("******")
        my_account = MyAccountSignedOut(self.driver)
        # go to my account
        my_account.go_to_my_account()
        # type username
        my_account.input_login_username('asdasdasd')
        # type password
        my_account.input_login_password('123456')
        # click login
        my_account.click_login_button()
        # verify error message
        expected_err = 'Error: The username asdasdasd is not registered on this site. If you are unsure of your username, try your email address instead.'
        my_account.wait_until_error_is_displayed(expected_err)
