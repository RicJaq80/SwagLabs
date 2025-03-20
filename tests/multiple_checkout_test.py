from pages.shop_checkout_page import ShopCheckoutPage
from pages.navigation import NavigationPage
from utilities.test_status import TestStatus
import utilities.custom_logger as cl
import unittest
import pytest
import logging

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class MultipleCheckout(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.multipleCheckout_methods = ShopCheckoutPage(self.driver)
        self.navigation = NavigationPage(self.driver)
        self.test_status = TestStatus()
    
    def test_select_products(self):
        self.log.info("Starting Products text Test")
        # products_page = self.shopCheckout_methods.verifyProductsPage()
        products_locator = "//span[.='Products']"
        products_page = self.multipleCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.mark(products_page, "Verify Products Page")

        self.log.info("Starting Select/Add To Cart Test")
        select_product = ["add-to-cart-sauce-labs-fleece-jacket",
                          "add-to-cart-sauce-labs-onesie"]
        self.multipleCheckout_methods.selectProduct(select_product)

        self.log.info("Starting Shopping Cart Added Product text Test")
        # shopping_cart = self.shopCheckout_methods.verifyShoppingCart()
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        shopping_cart = self.multipleCheckout_methods.verifyText(shopping_cart_badge, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Select Product Test",
                                   shopping_cart,
                                   "Verify Product is Selected")
    
    def test_your_cart(self):
        self.log.info("Starting Click on Shopping Cart Test")
        self.multipleCheckout_methods.clickShoppingCartButton()

        self.log.info("Starting Verify Your Cart text Step")
        # add_to_cart_text = self.shopCheckout_methods.verifyAddToCart()
        cart_locator = "//span[.='Your Cart']"
        add_to_cart_text = self.multipleCheckout_methods.verifyText(cart_locator, 
                                                                locatorType="xpath")
        self.test_status.mark(add_to_cart_text, "Verify Your Cart text")

        self.log.info("Starting Product Text Verification Step")
        description_locator = ["//div[.='Sauce Labs Fleece Jacket']", 
                               "//div[.='Sauce Labs Onesie']"]
        # your_cart_text = self.shopCheckout_methods.verifyDescription()
        for locator in description_locator:
            product_checkout = self.multipleCheckout_methods.verifyText(locator, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Your Cart Test", 
                                   product_checkout, "Verify Product Description Text")
