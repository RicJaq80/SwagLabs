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
n = 2

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
        global n

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
                                   cart_badge, "Verify Product Description Text")


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

    @pytest.mark.run(order=4)
    def test_checkout_overview_part1(self):
        self.log.info("Starting the Continue button step")
        self.multipleCheckout_methods.continueButton()

        self.log.info("Starting the Overview text Step")
        overview_locator = "//span[.='Checkout: Overview']"
        overview = self.multipleCheckout_methods.verifyText(overview_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(overview, "Verify Checkout Overview Text Step")

        self.log.info("Starting Product text Verification Step")
        product_locator = "(//div[@class='inventory_item_name'])[{0}]"
        product_checkout = self.multipleCheckout_methods.multipleGetText(n, product_locator, 
                                                                locatorType="xpath")
        result_product = self.multipleCheckout_methods.compareText(product_checkout, 
                                                                   product_cart_lst)
        self.test_status.mark(result_product, "Verify Product Name is Kept")

        self.log.info("Starting Price text Verification Step")
        amount_locator = "(//div[@class='inventory_item_price'])[{0}]"
        amount_checkout = self.multipleCheckout_methods.multipleGetText(n, amount_locator, 
                                                                locatorType="xpath")
        result_price = self.multipleCheckout_methods.compareText(amount_checkout, 
                                                                   amount_cart_lst)
        self.test_status.mark(result_product, "Verify Product Name is Kept")

        self.log.info("Starting Cart Badge Verification Step")
        cart_badge = self.multipleCheckout_methods.cartBadge(n)
        self.test_status.markFinal("Your Cart Badge Test", 
                                   cart_badge, "Verify Product Description Text")
    
    @pytest.mark.run(order=5)
    def test_checkout_overview_part2(self):
        w = "$"
        s = ": "
        new_lst = []

        self.log.info("Starting Subtotal Amount text Verification Step")
        subtotal_locator = "//div[@class='summary_subtotal_label']"
        subtotal_checkout = self.multipleCheckout_methods.getText(subtotal_locator,
                                                                  locatorType="xpath")
        _, _, subtotal_checkout_extract = subtotal_checkout.partition(w)
        # value of subtotal_checkout_extract: 57.980000000000004
        #convert to float the values of amount_cart_lst and sum them
        #  ['$49.99', '$7.99']
        for i in amount_cart_lst:
            _, _, subtotal_extract = i.partition(w)
            new_lst.append(float(subtotal_extract))
        subtotal_checkout_sum = sum(new_lst)
        result_subtotal = self.multipleCheckout_methods.compareText(str(subtotal_checkout_sum), 
                                                                    subtotal_checkout_extract)
        self.test_status.mark(result_subtotal, "Verify Subtotal Amount")

        self.log.info("Starting Total Ammount text Verification Step")
        tax_locator = "//div[@class='summary_tax_label']"
        taxes = self.multipleCheckout_methods.getText(tax_locator, locatorType="xpath")
        _, _, tax = taxes.partition(w)

        total_locator = "//div[@class='summary_total_label']"
        total_checkout = self.multipleCheckout_methods.getText(total_locator, locatorType="xpath")
        _, _, total = total_checkout.partition(w)

        total_amount = subtotal_checkout_sum + float(tax)
        total_amount_string = str(total_amount)
        result_total = self.multipleCheckout_methods.compareText(total_amount_string[:5], total)
        self.test_status.markFinal("Compare Amounts", result_total, "Verify Total Amount")

    @pytest.mark.run(order=6)
    def test_checkout_complete(self):
        self.log.info("Finish the Select Product Valid Test")
        self.multipleCheckout_methods.checkoutFinish()

        self.log.info("Starting the Checkout Complete text test")
        complete_locator = "//span[.='Checkout: Complete!']"
        complete = self.multipleCheckout_methods.verifyText(complete_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(complete, "Verify Checkout Complete text step")

        self.log.info("Starting the Thank You text step")
        thankyou_locator = "//h2[normalize-space()='Thank you for your order!']"
        thankyou = self.multipleCheckout_methods.verifyText(thankyou_locator, 
                                                        locatorType="xpath")
        self.test_status.mark(thankyou, "Verify the Thank you text Step")
        
        self.log.info("Starting the Back Home step")
        self.multipleCheckout_methods.checkoutComplete()
        time.sleep(2)

        self.log.info("Starting Products text Test")
        products_locator = "//span[.='Products']"
        products_page = self.multipleCheckout_methods.verifyText(products_locator, 
                                                             locatorType="xpath")
        self.test_status.markFinal("Checkout Complete Test", 
                                   products_page, "Verify Products Page")
        
        self.navigation.navigationMenu()
        self.navigation.navigationLogOut()
        time.sleep(2)
