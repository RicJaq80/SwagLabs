from base.selenium_driver import SeleniumMethods
import time

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
    
    ###################################
    # Methods to perform actions
    ###################################
    def enterUserName(self, userName):
        self.elementSendKeys(userName, self.user_name_field)

    def enterPassword(self, password):
        self.elementSendKeys(password, self.password_field)
    
    def clickLoginButton(self):
        self.elementClick(self.login_button)
    
    def login(self, userName, password):
        self.clearFields()
        self.enterUserName(userName)
        self.enterPassword(password)
        self.clickLoginButton()
    
    def verifyLogin(self):
        webTitleLocator = "//div[@class='app_logo']"
        result = self.elementText(webTitleLocator, locatorType="xpath")
        return result
    
    def verifyLoginInvalid(self):
        error_locator = "h3[data-test='error']"
        result = self.isElementPresent(error_locator, locatorType="css")
        return result
    
    def clearFields(self):
        clearUsernameField = self.getElement(locator=self.user_name_field)
        clearUsernameField.clear()
        result = self.waitForElement(self.password_field)
        clearPasswordField = self.getElement(locator=self.password_field)
        clearPasswordField.clear()

    def logoutSession(self):
        select_menu = "react-burger-menu-btn"
        select_logout = "logout_sidebar_link"
        self.elementClick(select_menu, locatorType="id")
        self.elementClick(select_logout, locatorType="id")
        time.sleep(2)
