from base.common_page import CommonPage
import time

class ShopCheckoutPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    ##########################################
    # LOCATORS from select product to checkout
    ##########################################
    select_product = "add-to-cart-sauce-labs-fleece-jacket"
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

    #####################################################
    # Actions on Locators from select product to checkout
    #####################################################
    def clickSelectProduct(self):
        self.elementClick(self.select_product)
    
    def clickShoppingCart(self):
        self.elementClick(self.shopping_cart, locatorType="xpath")
    
    def clickCheckoutButton(self):
        self.elementClick(self.checkout_button, locatorType="xpath")
    
    #######################################################
    # Actions on Locators to introduce customer information
    #######################################################
    def sendFirstName(self, first_name):
        self.elementSendKeys(first_name, self.first_name_locator)

    def sendLastName(self, first_name):
        self.elementSendKeys(first_name, self.last_name_locator)
    
    def sendPostalCode(self, first_name):
        self.elementSendKeys(first_name, self.postal_code_locator)
    
    def clickContinueButton(self):
        self.elementClick(self.continue_locator)
    
    def clickFinishButton(self):
        self.elementClick(self.finish_locator, locatorType="xpath")
    
    def clickBackHomeButton(self):
        self.elementClick(self.back_locator)
    
    ############################################################
    # Method that calls actions from select product to checkout
    ############################################################
    def selectProduct(self):
        self.clickSelectProduct()
        time.sleep(1)
    
    def clickShoppingCartButton(self):
        self.clickShoppingCart()
        time.sleep(1)
    
    def selectCheckout(self):
        self.clickCheckoutButton()
    
    ############################################################
    # Method that calls actions to add customer information
    ############################################################
    def checkoutInformation(self, first_name, last_name, postal_code):
        self.sendFirstName(first_name)
        self.sendLastName(last_name)
        self.sendPostalCode(postal_code)
        time.sleep(1)
    
    def continueButton(self):
        self.clickContinueButton()
        time.sleep(1)
    
    def checkoutFinish(self):
        self.clickFinishButton()
    
    def checkoutComplete(self):
        self.clickBackHomeButton()
    
    ######################################
    # General Function to Verify Text
    ######################################
    def verifyText(self, locator, locatorType="id"):
        return super().verifyText(locator, locatorType)
    
    ######################################
    # Verify we landed at Products page after login
    ######################################
    """
    def verifyProductsPage(self):
        products = "//span[.='Products']"
        result = self.isElementPresent(products, locatorType="xpath")
        return result
    """

    ######################################
    # Verify product added to the shopping cart
    ######################################
    """
    def verifyShoppingCart(self):
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        result = self.isElementPresent(shopping_cart_badge, locatorType="xpath")
        return result
    """

    ######################################
    # Verify the Your Cart text
    ######################################    
    """
    def verifyAddToCart(self):
        cart_locator = "//span[.='Your Cart']"
        result = self.isElementPresent(cart_locator, locatorType="xpath")
        return result
    """

    ######################################
    # Verify the selected product text
    ######################################
    """
    def verifyDescription(self):
        description = "//div[.='Sauce Labs Fleece Jacket']"
        result = self.isElementPresent(description, locatorType="xpath")
        return result
    """

    ######################################
    # Verify the Your Information text
    ######################################
    """
    def confirmInformationPage(self):
        confirm_page = "//span[.='Checkout: Your Information']"
        result = self.isElementPresent(confirm_page, locatorType="xpath")
        return result
    """
    
    ######################################
    # Verify the Checkout Overview text
    ######################################    
    """
    def verifyCheckoutOverview(self):
        overview_locator = "//span[.='Checkout: Overview']"
        result = self.isElementPresent(overview_locator, locatorType="xpath")
        return result
    """

    ######################################
    # Verify the Checkout Complete text
    ######################################   
    """ 
    def verifyCheckoutComplete(self):
        complete_locator = "//span[.='Checkout: Complete!']"
        result = self.isElementPresent(complete_locator, locatorType="xpath")
        return result
    """
    
    ######################################
    # Verify the Thank You text
    ######################################    
    """
    def verifyThankyou(self):
        thankyou_locator = "//h2[normalize-space()='Thank you for your order!']"
        result = self.isElementPresent(thankyou_locator, locatorType="xpath")
        return result
    """
