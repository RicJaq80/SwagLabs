from pages.shop_checkout_page import ShopCheckoutPage
from pages.navigation import NavigationPage
from utilities.test_status import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging
import time

global amount

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class ShopCheckoutTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.shopCheckout_methods = ShopCheckoutPage(self.driver)
        self.navigation = NavigationPage(self.driver)
        self.test_status = TestStatus()

    @pytest.mark.run(order=1)
    def test_select_product(self):
        self.log.info("Starting Products text Test")
        products_locator = "//span[.='Products']"
        products_page = self.shopCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.mark(products_page, "Verify Products Page")

        self.log.info("Starting Select/Add To Cart Test")
        select_product = ["add-to-cart-sauce-labs-fleece-jacket"]
        self.shopCheckout_methods.selectProduct(select_product)

        self.log.info("Starting Shopping Cart Added Product text Test")
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        shopping_cart = self.shopCheckout_methods.verifyText(shopping_cart_badge, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Select Product Test",
                                   shopping_cart,
                                   "Verify Product is Selected")

    
    @pytest.mark.run(order=2)
    def test_your_cart(self):
        global amount_cart
        global product_cart

        self.log.info("Starting Click on Shopping Cart Test")
        self.shopCheckout_methods.clickShoppingCartButton()

        self.log.info("Starting Verify Your Cart text Step")
        cart_locator = "//span[.='Your Cart']"
        add_to_cart_text = self.shopCheckout_methods.verifyText(cart_locator, 
                                                                locatorType="xpath")
        self.test_status.mark(add_to_cart_text, "Verify Your Cart text")

        self.log.info("Starting Price text Verification Step")
        amount_locator = "//div[@class='inventory_item_price']"
        amount_cart = self.shopCheckout_methods.getText(amount_locator, locatorType="xpath")

        self.log.info("Starting Product text Verification Step")
        product_locator = "//div[@class='inventory_item_name']"
        product_cart = self.shopCheckout_methods.getText(product_locator, locatorType="xpath")

        self.log.info("Starting Product Text Verification Step")
        description_locator = "//div[.='Sauce Labs Fleece Jacket']"
        product_checkout = self.shopCheckout_methods.verifyText(description_locator, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Your Cart Test", 
                                   product_checkout, "Verify Product Description Text")


    @pytest.mark.run(order=3)
    def test_checkout_information(self):
        self.log.info("Starting YourCart Test")
        self.shopCheckout_methods.selectCheckout()

        self.log.info("Starting Checkout Information Test")
        self.shopCheckout_methods.checkoutInformation()
        
        self.log.info("Starting Your Information text Step")
        confirm_page = "//span[.='Checkout: Your Information']"
        your_information = self.shopCheckout_methods.verifyText(confirm_page, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Customer Information Test", 
                                   your_information, "Verify Customer Information")
        
    
    @pytest.mark.run(order=4)
    def test_checkout_overview_part1(self):
        self.log.info("Starting the Continue button step")
        self.shopCheckout_methods.continueButton()

        self.log.info("Starting the Overview text Step")
        overview_locator = "//span[.='Checkout: Overview']"
        overview = self.shopCheckout_methods.verifyText(overview_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(overview, "Verify Checkout Overview Text Step")

        self.log.info("Starting Product text Verification Step")
        product_locator = "//div[@class='inventory_item_name']"
        product_checkout = self.shopCheckout_methods.getText(product_locator, locatorType="xpath")
        result_product = self.shopCheckout_methods.compareText(product_cart, product_checkout)
        self.test_status.mark(result_product, "Verify Product Name is Kept")

        self.log.info("Starting Price text Verification Step")
        amount_locator = "//div[@class='inventory_item_price']"
        amount_checkout = self.shopCheckout_methods.getText(amount_locator, locatorType="xpath")
        result_amount = self.shopCheckout_methods.compareText(amount_cart, amount_checkout)
        self.test_status.mark(result_amount, "Verify Amount is Kept")

    @pytest.mark.run(order=5)
    def test_checkout_overview_part2(self):
        w = "$"
        s = ": "
    
        self.log.info("Starting Subtotal Amount text Verification Step")
        subtotal_locator = "//div[@class='summary_subtotal_label']"
        subtotal_checkout = self.shopCheckout_methods.getText(subtotal_locator, locatorType="xpath")
        _, _, subtotal_checkout_extract = subtotal_checkout.partition(s)
        result_subtotal = self.shopCheckout_methods.compareText(amount_cart, subtotal_checkout_extract)
        self.test_status.mark(result_subtotal, "Verify Subtotal Amount")

        self.log.info("Starting Total Amount text Verification Step")
        total_locator = "//div[@class='summary_total_label']"
        total_checkout = self.shopCheckout_methods.getText(total_locator, locatorType="xpath")
        tax_locator = "//div[@class='summary_tax_label']"
        taxes = self.shopCheckout_methods.getText(tax_locator, locatorType="xpath")
        _, _, subtotal_extract = subtotal_checkout_extract.partition(w)
        _, _, total = total_checkout.partition(w)
        _, _, tax = taxes.partition(w)
        total_amount = float(subtotal_extract) + float(tax)
        result_total = self.shopCheckout_methods.compareText(str(total_amount), total)
        self.test_status.mark(result_total, "Verify Total Amount")
        
        self.log.info("Starting Added Product text Step")
        description_locator = "//div[.='Sauce Labs Fleece Jacket']"
        product_checkout = self.shopCheckout_methods.verifyText(description_locator, 
                                                                locatorType="xpath")
        self.test_status.markFinal("Checkout Overview Text", 
                                   product_checkout, "Verify the Added Product text Step")
        
    
    @pytest.mark.run(order=6)
    def test_checkout_complete(self):
        self.log.info("Finish the Select Product Valid Test")
        self.shopCheckout_methods.checkoutFinish()

        self.log.info("Starting the Checkout Complete text test")
        complete_locator = "//span[.='Checkout: Complete!']"
        complete = self.shopCheckout_methods.verifyText(complete_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(complete, "Verify Checkout Complete text step")

        self.log.info("Starting the Thank You text step")
        thankyou_locator = "//h2[normalize-space()='Thank you for your order!']"
        thankyou = self.shopCheckout_methods.verifyText(thankyou_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(thankyou, "Verify the Thank you text Step")
        
        self.log.info("Starting the Back Home step")
        self.shopCheckout_methods.checkoutComplete()
        time.sleep(2)

        self.log.info("Starting Products text Test")
        products_locator = "//span[.='Products']"
        products_page = self.shopCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Checkout Complete Test", 
                                   products_page, "Verify Products Page")
        
        self.navigation.navigationMenu()
        self.navigation.navigationLogOut()
        time.sleep(2)
