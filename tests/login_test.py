<<<<<<< HEAD
from selenium import webdriver
=======
# from selenium import webdriver
# from selenium.webdriver.common.by import By
>>>>>>> 555d9278d76256233946c616b2daf8da582efe9f
from pages.login_page import LoginPage
import unittest
import time
import pytest

@pytest.mark.usefixtures("ClassSetup", "MethodSetup")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetUp(self):
        self.login_methods = LoginPage(self.driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        userName = "standard_user"
        password = ""

        self.login_methods.login(userName, password)
        time.sleep(1)

        webTitle = "Swag Labs"
        webTitleLocator = "//div[@class='app_logo']"
        result = self.login_methods.verifyLogin(webTitleLocator)
        assert result == webTitle


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        userName = "standard_friend"
        password = "secret_sauce"

        self.login_methods.login(userName, password)
        time.sleep(3)

        error_locator = "h3[data-test='error']"
        result = self.login_methods.verifyLoginInvalid(error_locator)
        assert result == True
