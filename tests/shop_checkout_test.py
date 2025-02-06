from pages.shop_checkout_page import ShopCheckoutPage
from utilities.test_status import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class ShopCheckoutTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.shopCheckout_methods = ShopCheckoutPage(self.driver)
        self.test_status = TestStatus()

    @pytest.mark.run(order=1)
    def test_select_product(self):
        self.log.info("Starting Products text Test")
        # products_page = self.shopCheckout_methods.verifyProductsPage()
        products_locator = "//span[.='Products']"
        products_page = self.shopCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.mark(products_page, "Verify Products Page")

        self.log.info("Starting Select/Add To Cart Test")
        self.shopCheckout_methods.selectProduct()

        self.log.info("Starting Shopping Cart Added Product text Test")
        # shopping_cart = self.shopCheckout_methods.verifyShoppingCart()
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        shopping_cart = self.shopCheckout_methods.verifyText(shopping_cart_badge, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Select Product Test",
                                   shopping_cart,
                                   "Verify Product is Selected")

    
    @pytest.mark.run(order=2)
    def test_your_cart(self):
        self.log.info("Starting Click on Shopping Cart Test")
        self.shopCheckout_methods.clickShoppingCartButton()

        self.log.info("Starting Verify Your Cart text Step")
        # add_to_cart_text = self.shopCheckout_methods.verifyAddToCart()
        cart_locator = "//span[.='Your Cart']"
        add_to_cart_text = self.shopCheckout_methods.verifyText(cart_locator, 
                                                                locatorType="xpath")
        self.test_status.mark(add_to_cart_text, "Verify Your Cart text")

        self.log.info("Starting Product Text Verification Step")
        description_locator = "//div[.='Sauce Labs Fleece Jacket']"
        # your_cart_text = self.shopCheckout_methods.verifyDescription()
        product_checkout = self.shopCheckout_methods.verifyText(description_locator, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Your Cart Test", 
                                   product_checkout, "Verify Product Description Text")


    @pytest.mark.run(order=3)
    def test_checkout_information(self):
        first_name = "Tony"
        last_name = "Jones"
        postal_code = "90210"

        self.log.info("Starting YourCart Test")
        self.shopCheckout_methods.selectCheckout()

        self.log.info("Starting Checkout Information Test")
        self.shopCheckout_methods.checkoutInformation(first_name, last_name, postal_code)
        
        self.log.info("Starting Your Information text Step")
        confirm_page = "//span[.='Checkout: Your Information']"
        # your_information = self.shopCheckout_methods.confirmInformationPage()
        your_information = self.shopCheckout_methods.verifyText(confirm_page, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Customer Information Test", 
                                   your_information, "Verify Customer Information")
        
    
    @pytest.mark.run(order=4)
    def test_checkout_overview(self):
        self.log.info("Starting the Continue button step")
        self.shopCheckout_methods.continueButton()

        self.log.info("Starting the Overview text Step")
        # overview = self.shopCheckout_methods.verifyCheckoutOverview()
        overview_locator = "//span[.='Checkout: Overview']"
        overview = self.shopCheckout_methods.verifyText(overview_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(overview, "Verify Checkout Overview Text Step")

        self.log.info("Starting Added Product text Step")
        # product = self.shopCheckout_methods.verifyDescription()
        description_locator = "//div[.='Sauce Labs Fleece Jacket']"
        product_checkout = self.shopCheckout_methods.verifyText(description_locator, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Checkout Overview Text", 
                                   product_checkout, "Verify the Added Product text Step")
        
    
    @pytest.mark.run(order=5)
    def test_checkout_complete(self):
        self.log.info("Finish the Select Product Valid Test")
        self.shopCheckout_methods.checkoutFinish()

        self.log.info("Starting the Checkout Complete text test")
        complete_locator = "//span[.='Checkout: Complete!']"
        # complete = self.shopCheckout_methods.verifyCheckoutComplete()
        complete = self.shopCheckout_methods.verifyText(complete_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(complete, "Verify Checkout Complete text step")

        self.log.info("Starting the Thank You text step")
        thankyou_locator = "//h2[normalize-space()='Thank you for your order!']"
        # thankyou = self.shopCheckout_methods.verifyThankyou()
        thankyou = self.shopCheckout_methods.verifyText(thankyou_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(thankyou, "Verify the Thank you text Step")
        
        self.log.info("Starting the Back Home step")
        self.shopCheckout_methods.checkoutComplete()

        self.log.info("Starting Products text Test")
        # products_page = self.shopCheckout_methods.verifyProductsPage()
        products_locator = "//span[.='Products']"
        products_page = self.shopCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Checkout Complete Test", 
                                   products_page, "Verify Products Page")
