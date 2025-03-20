import unittest
from tests.login_test import LoginTest
from tests.shop_checkout_test import ShopCheckoutTest

tc1 = unittest.TestLoader().loadTestsFromModule(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromModule(ShopCheckoutTest)

regressionTest = unittest.TestSuite([tc1,tc2])

unittest.TextTestRunner(verbosity=2).run(regressionTest)
