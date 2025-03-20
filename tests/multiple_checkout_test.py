from pages.shop_checkout_page import ShopCheckoutPage
from pages.navigation import NavigationPage
from utilities.test_status import TestStatus
import unittest
import pytest

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class MultipleCheckout(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.multipleCheckout_methods = ShopCheckoutPage(self.driver)
        self.navigation = NavigationPage(self.driver)
        self.test_status = TestStatus()
    
    def test_select_products(self):
        pass