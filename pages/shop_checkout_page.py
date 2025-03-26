from base.common_page import CommonPage
import time

class ShopCheckoutPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    ##########################################
    # LOCATORS from product page to checkout
    ##########################################
    shopping_cart = "//a[@class='shopping_cart_link']"
    checkout_button = "//button[@id='checkout']"

    ############################################
    # LOCATORS to add information after checkout
    ############################################
    first_name_locator = "first-name" # id
    last_name_locator = "last-name" # id
    postal_code_locator = "postal-code" # id
    continue_locator = "continue" # id
    finish_locator = "//button[@id='finish']" # xpath
    complete_locator = "//span[.='Checkout: Complete!']"
    thankyou_locator = "//h2[normalize-space()='Thank you for your order!']"
    back_locator = "back-to-products"

    ############################################################
    # Method that calls actions from select product to checkout
    ############################################################
    def selectProduct(self, clickLst):
        for element in clickLst:
            self.elementClick(element)
        time.sleep(1)
    
    def clickShoppingCartButton(self):
        self.elementClick(self.shopping_cart, locatorType="xpath")
        time.sleep(1)
    
    def selectCheckout(self):
        self.elementClick(self.checkout_button, locatorType="xpath")
    
    ############################################################
    # Method that calls actions to add customer information
    ############################################################
    def checkoutInformation(self, first_name, last_name, postal_code):
        self.elementSendKeys(first_name, self.first_name_locator)
        self.elementSendKeys(last_name, self.last_name_locator)
        self.elementSendKeys(postal_code, self.postal_code_locator)
        time.sleep(1)
    
    def continueButton(self):
        self.elementClick(self.continue_locator)
        time.sleep(1)
    
    def checkoutFinish(self):
        self.elementClick(self.finish_locator, locatorType="xpath")

    def checkoutComplete(self):
        self.elementClick(self.back_locator)
    
    ######################################
    # General Text Methods
    ######################################
    def getText(self, locator, locatorType):
        txt = self.elementText(locator, locatorType)
        return txt
    
    def verifyText(self, locator, locatorType):
        return self.verifyGeneralText(locator, locatorType)
    
    def compareText(self, txt1, txt2):
        if txt1 == txt2:
            return True
        else:
            return False
