from base.selenium_driver import SeleniumMethods

class CommonPage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
    
    def verifyGeneralText(self, locator, locatorType = "id"):
        try:
            received_text = self.isElementPresent(locator, locatorType)
            return received_text
        except:
            self.log.error("Failed to get the expected Text")
            return False
    
    def add_customer_information(self):
        first_name = "Tony"
        last_name = "Jones"
        postal_code = "90210"
        first_name_locator = "first-name" # id
        last_name_locator = "last-name" # id
        postal_code_locator = "postal-code" # id

        try:
            self.elementSendKeys(first_name, first_name_locator)
            self.elementSendKeys(last_name, last_name_locator)
            self.elementSendKeys(postal_code, postal_code_locator)
        except:
            self.log.error("Failed to Send the Customer Information")
