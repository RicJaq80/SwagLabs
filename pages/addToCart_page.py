from base.selenium_driver import SeleniumMethods

class AddToCartPage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #####################################
    # LOCATORS
    #####################################
    select_product = "add-to-cart-sauce-labs-fleece-jacket"
    shopping_cart = "//a[@class='shopping_cart_link']"
    description = "//div[.='Sauce Labs Fleece Jacket']"
    # checkout_button = "//button[@id='checkout']"

    #####################################
    # LOCATORS
    #####################################
    def clickSelectProduct(self):
        self.elementClick(self.select_product)
    
    def clickShoppingCart(self):
        self.elementClick(self.shopping_cart, locatorType="xpath")
    
    def getDescription(self):
        self.isElementPresent(self.description, locatorType="xpath")
    
    """
    def clickCheckoutButton(self):
        self.elementClick(self.checkout_button, locatorType="xpath")
    """
    
    def SelectCheckout(self):
        self.clickSelectProduct()
        self.clickShoppingCart()
        self.getDescription()
        # self.clickCheckoutButton()
    
    def verifyAddToCart(self):
        cart_locator = "//span[.='Your Cart']"
        result = self.isElementPresent(cart_locator, locatorType="xpath")
        return result
