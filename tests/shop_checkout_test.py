from selenium import webdriver
from pages.shop_checkout_page import ShopCheckoutPage
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
    
    @pytest.mark.run(order=1)
    def test_select_product(self):
        self.log.info("Starting Select/Add To Cart Test")
        self.shopCheckout_methods.selectProduct()

        add_to_cart_text = self.shopCheckout_methods.verifyAddToCart()
        assert add_to_cart_text == True

        self.log.info("Starting Product Text Verification Test")
        your_cart_text = self.shopCheckout_methods.verifyDescription()
        assert your_cart_text == True

        self.log.info("Starting YourCart Test")
        self.shopCheckout_methods.selectCheckout()

    @pytest.mark.run(order=2)
    def test_checkout_information(self):
        first_name = "Tony"
        last_name = "Jones"
        postal_code = "90210"
        self.log.info("Starting Your Information text Test")
        your_information = self.shopCheckout_methods.confirmInformationPage()
        assert your_information == True
        
        self.log.info("Stating Checkout Information Test")
        self.shopCheckout_methods.checkoutInformation(first_name, last_name, postal_code)

        