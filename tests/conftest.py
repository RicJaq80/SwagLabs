# from selenium import webdriver
from pages.login_page import LoginPage
import utilities.custom_logger as cl
import pytest
import logging
from base.webdriver_setup import WebDriverSetup

@pytest.fixture()
def MethodSetup():
    log = cl.customLogger(logging.DEBUG)
    log.info("Start Test Case")
    yield
    log.info("Finish Test Case")

@pytest.fixture(scope="class")
def ClassSetup(request, browser):
    log = cl.customLogger(logging.DEBUG)
    log.info("Start Class Module")

    driver_instance = WebDriverSetup(browser)
    driver = driver_instance.driver_setup()

    login_methods = LoginPage(driver)
    userName = "standard_user"
    password = "secret_sauce"
    log.info("Login on ConfTest")
    login_methods.login(userName, password)

    if request.cls is not None:
        request.cls.driver = driver
    
    yield driver
    driver.quit()
    log.info("Finish Class Module")

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture(scope="module")
def browser(request):
    return request.config.getoption("--browser")
