from selenium import webdriver
from pages.addToCart_page import AddToCartPage
import unittest
import time
import pytest

class AddToCartTest(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    addToCart_methods = AddToCartPage(driver)
    
    def test_select_product(self):
        self.driver.get(self.baseUrl)

        self.addToCart_methods.SelectCheckout()

        cart_locator = "//span[.='Your Cart']"
        result = self.addToCart_methods.verifyAddToCart(cart_locator)
        assert result == True
