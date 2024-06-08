from selenium.webdriver.common.by import By
from constants import CartConstants

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class CartPage(BasePage):
    # ... (other methods remain unchanged)

    def add_item_to_cart(self, item_name, wait_for_cart=True, wait_for_button=True):
        # Click on the item to view details
        item_xpath = CartConstants.ITEM_NAME_XPATH.format(item_name)
        self.driver.find_element(By.XPATH, item_xpath).click()

        # Add the item to the cart
        if wait_for_button:
            wait_for_element_clickable(self.driver, By.XPATH, CartConstants.ADD_TO_CART_BUTTON_XPATH).click()
        else:
            self.driver.find_element(By.XPATH, CartConstants.ADD_TO_CART_BUTTON_XPATH).click()

        # Wait for the cart to update
        if wait_for_cart:
            self.go_to_cart()

    def get_cart_items(self):
        self.go_to_cart()
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        return [item.text for item in items]

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.CLASS_NAME, "checkout_button").click()

    def fill_shipping_information(self, first_name, last_name, zip_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys(zip_code)
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()

    def complete_purchase(self):
        self.driver.find_element(By.CLASS_NAME, "cart_button").click()


def add_items_to_cart(cart_page, *item_names):
    for item_name in item_names:
        cart_page.add_item_to_cart(item_name)

def perform_checkout(cart_page, first_name, last_name, zip_code):
    cart_page.go_to_cart()
    cart_page.proceed_to_checkout()
    cart_page.fill_shipping_information(first_name, last_name, zip_code)
    cart_page.complete_purchase()