from base.selenium_driver import SeleniumMethods

class CommonPage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
    
    def verifyText(self, locator, locatorType = "id"):
        try:
            received_text = self.isElementPresent(locator, locatorType)
            return received_text
        except:
            self.log.error("Failed to get the expected Text")
            return False
