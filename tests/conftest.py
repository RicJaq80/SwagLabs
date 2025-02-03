from selenium import webdriver
from pages.login_page import LoginPage
import utilities.custome_logger as cl
import pytest
import logging

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
    baseUrl = "https://www.saucedemo.com/"
    if browser == "chrome":
        log.info("Running on Chrome")
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseUrl)

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
