from selenium.webdriver.common.by import By

# Page Object for the Landing page
class LandingPage:
    def __init__(self, driver):
        self.driver = driver
        self.inventory_element = (By.CLASS_NAME, "inventory_list")
        self.cart_icon = (By.CLASS_NAME, "shopping_cart_container")
        self.filter_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.menu_button = (By.ID, "react-burger-menu-btn")

    def verify_elements_displayed(self):
        assert self.driver.find_element(*self.inventory_element).is_displayed()
        assert self.driver.find_element(*self.cart_icon).is_displayed()
        assert self.driver.find_element(*self.filter_dropdown).is_displayed()
        assert self.driver.find_element(*self.menu_button).is_displayed()

    def is_on_page(self):
        # Check if the inventory element is present on the landing page
        return self.driver.find_element(*self.inventory_element).is_displayed()
