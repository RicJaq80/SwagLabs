from selenium import webdriver
from pages.addToCart_page import AddToCartPage
import unittest
import pytest

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class AddToCartTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.addToCart_methods = AddToCartPage(self.driver)
    
    def test_select_product(self):

        self.addToCart_methods.SelectCheckout()

        
        result = self.addToCart_methods.verifyAddToCart()
        assert result == True
