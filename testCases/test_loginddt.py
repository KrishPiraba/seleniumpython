import pytest
from selenium import webdriver
from pageObjects.LoginPage import login
from utilities import ExcelUtils
from utilities.readConfig import ReadConfig
from utilities.customlogger import LogGen
from utilities.ExcelUtils import getRowCount


class Test_001_DDT_login:
    baseURL = ReadConfig.getApplicationURL()
    path=".//TestData.LoginData.xls"
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger=LogGen.loggen()

    def test_login_ddt(self,setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=login(self.driver)
        self.rows=ExcelUtils.getRowCount(self.path,'sheet1')

        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.get.title
        self.driver.close()
