from selenium import webdriver
from pages.addToCart_page import AddToCartPage
import unittest
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class AddToCartTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.addToCart_methods = AddToCartPage(self.driver)
    
    def test_select_product(self):
        self.log.info("Starting Add To Cart Test")
        self.addToCart_methods.SelectCheckout()
        self.log.info("Starting Verification of Add To Cart Test")
        result = self.addToCart_methods.verifyAddToCart()
        assert result == True
