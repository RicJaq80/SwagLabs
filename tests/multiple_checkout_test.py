from pages.shop_checkout_page import ShopCheckoutPage
from pages.navigation import NavigationPage
from utilities.test_status import TestStatus
import utilities.custom_logger as cl
import unittest
import pytest
import logging
import time

amount_cart_lst = []
product_cart_lst = []

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class MultipleCheckout(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.multipleCheckout_methods = ShopCheckoutPage(self.driver)
        self.navigation = NavigationPage(self.driver)
        self.test_status = TestStatus()
    

    @pytest.mark.run(order=1)
    def test_select_products(self):
        self.log.info("Starting Products text Test")
        products_locator = "//span[.='Products']"
        products_page = self.multipleCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.mark(products_page, "Verify Products Page")
        
        self.log.info("Starting Select/Add To Cart Test")
        select_product = ["add-to-cart-sauce-labs-fleece-jacket",
                          "add-to-cart-sauce-labs-onesie"]
        self.multipleCheckout_methods.selectProduct(select_product)

        self.log.info("Starting Shopping Cart Added Product text Test")
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        shopping_cart = self.multipleCheckout_methods.verifyText(shopping_cart_badge, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Select Product Test",
                                   shopping_cart,
                                   "Verify Product is Selected")


    @pytest.mark.run(order=2)
    def test_your_cart(self):
        global amount_cart_lst
        global product_cart_lst
        n = 2

        self.log.info("Starting Click on Shopping Cart Test")
        self.multipleCheckout_methods.clickShoppingCartButton()

        self.log.info("Starting Verify Your Cart text Step")
        cart_locator = "//span[.='Your Cart']"
        add_to_cart_text = self.multipleCheckout_methods.verifyText(cart_locator, 
                                                                locatorType="xpath")
        self.test_status.mark(add_to_cart_text, "Verify Your Cart text")

        self.log.info("Starting Price get text")
        amount_locator = "(//div[@class='inventory_item_price'])[{0}]"
        amount_cart_lst = self.multipleCheckout_methods.multipleGetText(n, amount_locator, 
                                                                        locatorType="xpath")

        self.log.info("Starting Product get text")
        product_locator = "(//div[@class='inventory_item_name'])[{0}]"
        product_cart_lst = self.multipleCheckout_methods.multipleGetText(n, product_locator, 
                                                                        locatorType="xpath")

        self.log.info("Starting Product Text Verification Step")
        description_locator = ["//div[.='Sauce Labs Fleece Jacket']", 
                               "//div[.='Sauce Labs Onesie']"]
        for locator in description_locator:
            product_checkout = self.multipleCheckout_methods.verifyText(locator, 
                                                                locatorType="xpath")
            self.test_status.mark(product_checkout, "Verify Your Cart text")
        
        self.log.info("Starting Cart Badge Verification Step")
        cart_badge = self.multipleCheckout_methods.cartBadge(n)
        self.test_status.markFinal("Your Cart Badge Test", 
                                   product_checkout, "Verify Product Description Text")


    @pytest.mark.run(order=3)
    def test_checkout_information(self):
        self.log.info("Starting YourCart Test")
        self.multipleCheckout_methods.selectCheckout()

        self.log.info("Starting Checkout Information Test")
        self.multipleCheckout_methods.checkoutInformation()
        time.sleep(2)
        
        self.log.info("Starting Your Information text Step")
        confirm_page = "//span[.='Checkout: Your Information']"
        your_information = self.multipleCheckout_methods.verifyText(confirm_page, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Customer Information Test", 
                                   your_information, "Verify Customer Information")   


