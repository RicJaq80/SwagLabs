from base.selenium_driver import SeleniumMethods
import time

class ShopCheckoutPage(SeleniumMethods):

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
        self.clickContinueButton()
        time.sleep(1)
    
    ######################################
    # Verify we landed at Products page after login
    ######################################
    def verifyProductsPage(self):
        products = "//span[.='Products']"
        result = self.isElementPresent(products, locatorType="xpath")
        return result

    ######################################
    # Verify product added to the shopping cart
    ######################################
    def verifyShoppingCart(self):
        shopping_cart_badge = "//span[@class='shopping_cart_badge']"
        result = self.isElementPresent(shopping_cart_badge, locatorType="xpath")
        return result

    ######################################
    # Verify the selected product text
    ######################################
    def verifyDescription(self):
        description = "//div[.='Sauce Labs Fleece Jacket']"
        result = self.isElementPresent(description, locatorType="xpath")
        return result

    ######################################
    # Verify the Your Cart text
    ######################################    
    def verifyAddToCart(self):
        cart_locator = "//span[.='Your Cart']"
        #cart_locator = "//span[@class='title']"
        result = self.isElementPresent(cart_locator, locatorType="xpath")
        return result

    ######################################
    # Verify the Your Information text
    ######################################
    def confirmInformationPage(self):
        # confirm_page = "//span[@class='title']"
        confirm_page = "//span[.='Checkout: Your Information']"
        result = self.isElementPresent(confirm_page, locatorType="xpath")
        return result
