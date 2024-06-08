from login_page import LoginPage
from landing_page import LandingPage

# Test Case 1: Verify successful login
# Test Case 1: Verify successful login
def test_successful_login(browser, login_page, landing_page, function):
    login_page.login("standard_user", "secret_sauce")
    landing_page.verify_elements_displayed()

# Test Case 2: Verify elements on the landing page after successful login
def test_successful_login_and_verify_elements(browser, login_page, landing_page, function):
    login_page.login("standard_user", "secret_sauce")
    landing_page.verify_elements_displayed()

# Test Case 3: Verify unsuccessful login with invalid credentials
def test_unsuccessful_login(browser, login_page, function):
    login_page.login("invalid_user", "invalid_password")

    error_message = login_page.get_error_message()
    assert "Username and password do not match any user in this service" in error_message

# Test Case 4: Verify unsuccessful login with empty credentials
def test_empty_credentials(browser, login_page, function):
    login_page.login("", "")

    error_message = login_page.get_error_message()
    assert "Username is required" in error_message
    assert "Epic sadface: Username is required" in error_message

# Test Case 5: Check that the user is redirected to the correct landing page after successful login
def test_successful_login_redirect(browser, login_page, landing_page, function):
    login_page.login("standard_user", "secret_sauce")

    # Implement is_on_page() method in LandingPage class
    assert landing_page.is_on_page()