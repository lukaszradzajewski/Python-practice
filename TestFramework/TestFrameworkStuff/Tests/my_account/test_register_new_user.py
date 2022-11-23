import pytest
from TestFramework.TestFrameworkStuff.src.pages.MyAccountSignedOut import MyAccountSignedOut
from TestFramework.TestFrameworkStuff.src.pages.MyAccountSignedIn import MyAccountSignedIn
from TestFramework.TestFrameworkStuff.src.helpers.generic_helpers import generate_random_email_and_password


@pytest.mark.usefixtures("init_driver")
class TestRegisterNewUser:

    @pytest.mark.tcid_2
    def test_register_valid_new_user(self):
        my_account_out = MyAccountSignedOut(self.driver)
        my_account_in = MyAccountSignedIn(self.driver)
        # go to my account
        my_account_out.go_to_my_account()
        # fill in email
        random_email = generate_random_email_and_password()
        my_account_out.input_register_email(random_email["email"])
        # fill in password
        my_account_out.input_register_password('asde1234!')
        # click register
        my_account_out.click_register_button()
        # verify user is registered
        my_account_in.verify_user_is_signed_in()
