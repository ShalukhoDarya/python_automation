from cart_page import CartPage, perform_checkout

# Test Case: Add to cart and checkout
def test_add_to_cart_and_checkout(browser, login, cart, function):
    # Access login_page and cart_page directly through fixtures
    cart_page = cart

    def test_add_item_to_cart(browser):
        item_name = "Sauce Labs Backpack"
        cart_page.add_item_to_cart(item_name)

        assert item_name in cart_page.get_cart_items()

    # Reusable function to perform checkout
    perform_checkout(cart_page, "Peter", "Pen", "12345")

    # Verify the purchase is successful
    assert "Thank you for your order" in browser.page_source
