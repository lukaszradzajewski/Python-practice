import pytest

pytestmark = pytest.mark.frontend


@pytest.mark.smoke
def test_login_page_valid_user():
    print("")
    print("Login with valid user")


@pytest.mark.regression
def test_login_wrong_password():
    print("Login with wrong password")
