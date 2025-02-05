from pages.login_page import LoginPage
from utilities.test_status import TestStatus
import unittest
import time
import pytest
import utilities.custom_logger as cl
import logging

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class LoginTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.login_methods = LoginPage(self.driver)
        self.test_status = TestStatus()

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        
        userName = "standard_user"
        password = ""
        self.log.info("Running Valid Login")
        self.login_methods.login(userName, password)
        
        time.sleep(1)
        webTitle = "Swag Labs"
        self.log.info("Running Verification of Login")
        result = self.login_methods.verifyLogin()
        time.sleep(1)
        # assert result == webTitle
        self.test_status.markFinal("Verification Valid Login", result, "Valid Login")


    @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="test valid for now")
    def test_invalid_login(self):
        self.log.info("Running Logout for Invalid Test")
        self.login_methods.logoutSession()

        userName = "standard_friend"
        password = "secret_sauce"

        time.sleep(1)
        self.log.info("Running Invalid Login")
        self.login_methods.login(userName, password)
        time.sleep(1)

        result = self.login_methods.verifyLoginInvalid()
        time.sleep(1)
        self.test_status.markFinal("Verfication Invalid Login", result, "Invalid Login")
