import pytest
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.LoginPage import Login
from utilities import XLutils
from utilities.Readconfigfile import ReadValue
from utilities.Logger import LogGen

class Test_Login_DDT:
    Url= ReadValue.getUrl()
    log = LogGen.loggen()
    path= "C:\\Users\\HP\\OneDrive\\Desktop\\letskodeit\\TestData\\LoginData.xlsx"

    def test_login_ddt_003(self, setup, getDataForLogin):
        self.log.info(" Opening Browser ")
        self.driver = setup
        self.driver.get(self.Url)
        self.log.info(" Going to Url")
        self.lp = Login(self.driver)
        self.rows = XLutils.getrowCount(self.path, 'Sheet1')
        print("Number of rows are ---> ", self.rows)
        login_status=[]
        for r in range(2, self.rows + 1):
            self.username = XLutils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLutils.readData(self.path, 'Sheet1', r,  2)
            self.Exp_Status = XLutils.readData(self.path, 'Sheet1', r, 3)
            self.lp.Enter_UserName(self.username)
            self.log.info("Enter_UserName"+ self.username)
            self.lp.Enter_Password(self.password)
            self.log.info("Enter_Password" + self.password)
            self.lp.Click_Login()
            self.log.info("Click on login Button" )
            self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_ddt_003_loginpage.png")
            login_status=[]
            if self.lp.login_status() == True:
                if self.Exp_Status == "Pass":
                    login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_ddt_003_Pass.png")
                self.lp.Click_Menu_Button()
                self.log.info(" Click on menu button ")
                self.lp.Click_logout_Button()
                self.log.info(" Click on Logout button ")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Pass")
            elif self.Exp_Status == "Fail":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_ddt_003_Pass.png")
                self.lp.Click_Menu_Button()
                self.log.info(" Click on menu button ")
                self.lp.Click_logout_Button()
                self.log.info(" Click on Logout button ")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
        else:
            if self.Exp_Status == "Fail":
                login_status.append("Pass")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_ddt_003_Fail.png")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")
            elif self.Exp_Status == "Pass":
                login_status.append("Fail")
                self.driver.save_screenshot("C:\\Users\HP\\OneDrive\\Desktop\\letskodeit\\Screenshots\\test_login_ddt_003_Fail.png")
                XLutils.writeData(self.path, 'Sheet1', r, 4, "Fail")

        print(login_status)

        if "Fail" not in login_status:
            self.log.info(" test_login_ddt_003 is Passed ")
            assert True
        else:
            self.log.info(" test_login_ddt_003 is Failed ")
            assert False
        self.driver.close()
        self.log.info(" test_login_ddt_003 is completed ")
        self.driver.quit()



# #   pytest -v -rA -s -n=4  testCases/test_login_ddt.py --browser chrome --html=Report/report.html