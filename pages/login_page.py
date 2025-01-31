# from selenium import webdriver
from selenium.webdriver.common.by import By
from base.selenium_driver import SeleniumMethods

class LoginPage(SeleniumMethods):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    #####################################
    # LOCATORS
    #####################################
    user_name_field = "user-name"
    password_field = "password"
    login_button = "login-button"
    
    """
    def login(self, userName, password):
        userNameField = self.driver.find_element(By.ID, self.user_name_field)
        userNameField.send_keys(userName)

        passwordField = self.driver.find_element(By.ID, self.password_field)
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.ID, self.login_button)
        loginButton.click()

    ###################################
    # Methods to get the locators
    ###################################
    def getUserNameField(self):
        return self.driver.find_element(By.ID, self.user_name_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self.password_field)
    
    def getLoginButton(self):
        return self.driver.find_element(By.ID, self.login_button)
    """
    ###################################
    # Methods to perform actions
    ###################################
    def enterUserName(self, userName):
        # self.getUserNameField().send_keys(userName)
        self.elementSendKeys(userName, self.user_name_field)

    
    def enterPassword(self, password):
        # self.getPasswordField().send_keys(password)
        self.elementSendKeys(password, self.password_field)
    
    def clickLoginButton(self):
        # self.getLoginButton().click()
        self.elementClick(self.login_button)
    
    def login(self, userName, password):
        self.clearFields()
        self.enterUserName(userName)
        self.enterPassword(password)
        self.clickLoginButton()
    
    def verifyLogin(self, webTitleLocator):
        # self.log.info("Locator (for verifyLogin): " + webTitleLocator)
        result = self.elementText(webTitleLocator, locatorType="xpath")
        return result
    
    def verifyLoginInvalid(self, locator):
        # self.log.info("Locator (for verifyLoginInvalid): " + locator)
        result = self.isElementPresent(locator, locatorType="css")
        return result
    
    def clearFields(self):
        clearUsernameField = self.getElement(locator=self.user_name_field)
        clearUsernameField.clear()
        clearPasswordField = self.getElement(locator=self.password_field)
        clearPasswordField.clear()

