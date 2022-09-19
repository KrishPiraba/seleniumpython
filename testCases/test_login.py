import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
from utilities.readConfig import ReadConfig
from utilities.customlogger import LogGen


class Test_001_login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()
    def test_homepageTitle(self,pytestconfig):
        self.logger.info("*******************TestCASE Passed*************")
        self.driver = pytestconfig
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title == "Your store. Login":
            assert True
            self.logger.info("*****************test case passed***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            assert False
    def test_login(self,setup):
        self.driver = setup()
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.get.title
        self.driver.close()
