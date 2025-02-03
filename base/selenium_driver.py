from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import utilities.custom_logger as cl
import logging

class SeleniumMethods():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
    
    def getByType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "name":
            return By.NAME
        else:
            # print("Locator Type: " + locatorType + " is not supported/valid")
            self.log.info("Locator Type: " + locatorType + " is not supported/valid")
        return False
    

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = self.getByType(locatorType)
            element = self.driver.find_element(locatorType, locator)
            # print("Locator: " + locator + " is found")
            self.log.info("Locator: " + locator + " is found")
        except:
            # print("Locator: " + locator + " is Not found")
            self.log.error("Locator: " + locator + " is Not found")
        return element
    

    def getElements(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = self.getByType(locatorType)
            element = self.driver.find_elements(locatorType, locator)
            # print("Locator: " + locator + " is found")
            self.log.info("Locator: " + locator + " is found")
        except:
            # print("Locator List: " + locator + " is NOT found")
            self.log.error("Locator List: " + locator + " is Not found")
        return element
    

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            # print("Element: " + locator + " is clickeable")
            self.log.info("Element: " + locator + " is clickeable")
        except:
            # print("Element: " + locator + " is NOT clickeable")
            self.log.error("Element: " + locator + " is NOT clickeable")
    
    def elementSendKeys(self, txt, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(txt)
            # print("Locator: " + locator + " received text: " + txt)
            self.log.info("Locator: " + locator + " received text: " + txt)
        except:
            # print("Locator: " + locator + " did NOT receive text: " + txt)
            self.log.error("Locator: " + locator + " did NOT receive text: " + txt)
    

    def isElementPresent(self, locator, locatorType):
        self.log.info("Running isElementPresent method")
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Locator: " + locator + " is Present")
                return True
            else:
                self.log.error("Locator: " + locator + " is Not Present")
                return False
        except:
            self.log.error("Locator: " + locator) + " is Not Found/Correct"
    

    def elementText(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            txt = element.text
            self.log.info("Element: " + locator + " has text: " + txt)
        except:
            self.log.error("Element: " + locator + " has not text/not found")
        return txt
    
    
    def waitForElement(self, locator, locatorType="id", timeout_1 = 10, 
                       poll_freq = 0.5):
        element = None
        try:
            byType = self.getByType(locatorType)
            self.log.info("Waiting for maximum of: " + str(timeout_1))
            wait = WebDriverWait(self.driver, timeout=timeout_1, poll_frequency=poll_freq,
                                 ignored_exceptions=[NoSuchElementException, 
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.visibility_of_element_located((byType, locator)))
            self.log.info("Element: " + str(element) + " appeared on the web page")
        except:
            self.log.error("Element: " + str(element) + " did Not appear on the web page")
        return element
