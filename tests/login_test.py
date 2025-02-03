# from selenium import webdriver
# from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import unittest
import time
import pytest
import utilities.custome_logger as cl
import logging

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class LoginTest(unittest.TestCase):

    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.login_methods = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        
        userName = "standard_user"
        password = ""
        self.log.info("Running Valid Login")
        self.login_methods.login(userName, password)
        

        time.sleep(2)
        webTitle = "Swag Labs"
        self.log.info("Running Verification of Login")
        result = self.login_methods.verifyLogin()
        assert result == webTitle


    @pytest.mark.run(order=1)
    # @pytest.mark.skip(reason="test valid for now")
    def test_invalid_login(self):
        self.log.info("Running Logout for Invalid Test")
        self.login_methods.logoutSession()

        userName = "standard_friend"
        password = "secret_sauce"

        time.sleep(2)
        self.log.info("Running Invalid Login")
        self.login_methods.login(userName, password)
        time.sleep(3)

        result = self.login_methods.verifyLoginInvalid()
        assert result == True
