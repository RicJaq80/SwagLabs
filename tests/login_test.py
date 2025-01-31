from selenium import webdriver
from pages.login_page import LoginPage
import unittest
import time
import pytest

class LoginTest(unittest.TestCase):
    baseUrl = "https://www.saucedemo.com/"
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    login_methods = LoginPage(driver)

    @pytest.mark.run(order=2)
    def test_valid_login(self):
        self.driver.get(self.baseUrl)

        userName = "standard_user"
        password = "secret_sauce"

        self.login_methods.login(userName, password)
        time.sleep(3)

        webTitle = "Swag Labs"
        webTitleLocator = "//div[@class='app_logo']"
        # element = self.driver.find_element(By.XPATH, webTitleLocator)
        result = self.login_methods.verifyLogin(webTitleLocator)
        assert result == webTitle

        self.driver.quit()


    @pytest.mark.run(order=1)
    def test_invalid_login(self):
        self.driver.get(self.baseUrl)

        userName = "standard_friend"
        password = "secret_sauce"

        self.login_methods.login(userName, password)
        time.sleep(3)

        # error_locator = "//h3[contains(text(),'Epic sadface: Username and password do not match any user in this service')]"
        error_locator = "h3[data-test='error']"
        result = self.login_methods.verifyLoginInvalid(error_locator)
        assert result == True
