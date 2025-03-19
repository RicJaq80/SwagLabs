from base.common_page import CommonPage


class NavigationPage(CommonPage):

    def __init__(self, driver):
        super().__init__(driver)
    
    #################################################
    # locator to logout
    #################################################
    menu = "react-burger-menu-btn" # ID
    logout = "logout_sidebar_link" # ID

    def navigationMenu(self):
        self.elementClick(self.menu, locatorType="id")
    
    def navigationLogOut(self):
        self.elementClick(self.logout, locatorType="id")
