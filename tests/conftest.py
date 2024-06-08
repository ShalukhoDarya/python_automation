import pytest
from selenium import webdriver
from login_page import LoginPage
from landing_page import LandingPage
from cart_page import CartPage

@pytest.fixture
def browser():
    driver = webdriver.Firefox()
    driver.get("https://www.saucedemo.com/")
    yield driver
    driver.quit()

# Fixture for the login page
@pytest.fixture
def login_page(browser):
    return LoginPage(browser)

# Fixture for the landing page
@pytest.fixture
def landing_page(browser):
    return LandingPage(browser)

@pytest.fixture
def login(browser):
    # Assuming you have a login method in your LoginPage class
    login_page = LoginPage(browser)
    login_page.login("your_username", "your_password")

@pytest.fixture
def cart(browser, login):
    # Assuming that navigating to the cart is part of the login process
    cart_page = CartPage(browser)
    return cart_page

# Fixture for setup and teardown actions before and after each test function
@pytest.fixture
def function():
    yield


