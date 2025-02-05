from selenium import webdriver
import utilities.custom_logger as cl
import logging

class WebDriverSetup():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, browser):
        self.browser = browser

    def driver_setup(self):
        baseUrl = "https://www.saucedemo.com/"
        if self.browser == "chrome":
           self.log.info("Running on Chrome")
           driver = webdriver.Chrome()
        elif self.browser == "firefox":
            self.log.info("Running on Firefox")
            driver = webdriver.Firefox()
        elif self.browser == "edge":
            self.log.info("Running on Edge")
            driver = webdriver.Edge()
        else:
            self.log.info("Running on Chrome")
            driver = webdriver.Chrome()
        driver.maximize_window()
        driver.implicitly_wait(2)
        driver.get(baseUrl)
        return driver
