from selenium import webdriver
class login:
    textbox_username_id="email"
    textbox_password_id="Password"
    button_login_xpath="//input[@class='button-1login-button']"
    link_logout_linktext="logout"
    def __init__(self,driver):
        self.driver = driver
    def setUserName(self,username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_idtextbox).send_keys(username)
    def setPassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)
    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()
    def clickLogout(self):
        self.driver.finf_element_by_linktesxt(self.link_logout_linktext).click()